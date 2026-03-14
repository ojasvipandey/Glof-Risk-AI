"""
Machine learning model for GLOF breach prediction.
"""

import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, Optional
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from utils.config import MODELS_DIR
from utils.helpers import generate_synthetic_ml_data


class BreachPredictionModel:
    """Random Forest model for predicting glacial lake breach probability."""
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize breach prediction model.
        
        Args:
            model_path: Path to saved model file
        """
        self.model = None
        self.label_encoder = LabelEncoder()
        self.model_path = Path(model_path) if model_path else Path(MODELS_DIR) / "breach_model.pkl"
        self.is_trained = False
        
        # Load model if it exists
        if self.model_path.exists():
            self.load_model()
        else:
            # Train on synthetic data if model doesn't exist
            self.train_model()
    
    def prepare_features(self, data: pd.DataFrame) -> np.ndarray:
        """
        Prepare features for model training/prediction.
        
        Args:
            data: DataFrame with raw features
        
        Returns:
            NumPy array of prepared features
        """
        features = data.copy()
        
        # Encode categorical variable
        if 'dam_type' in features.columns:
            if not hasattr(self.label_encoder, 'classes_'):
                features['dam_type_encoded'] = self.label_encoder.fit_transform(features['dam_type'])
            else:
                # Handle unseen categories
                known_categories = set(self.label_encoder.classes_)
                features['dam_type'] = features['dam_type'].apply(
                    lambda x: x if x in known_categories else self.label_encoder.classes_[0]
                )
                features['dam_type_encoded'] = self.label_encoder.transform(features['dam_type'])
        
        # Select feature columns
        feature_cols = [
            'lake_area', 'lake_volume', 'dam_type_encoded',
            'rainfall_intensity', 'terrain_slope', 'temperature_anomaly'
        ]
        
        return features[feature_cols].values
    
    def train_model(self, n_samples: int = 1000):
        """
        Train Random Forest model on synthetic data.
        
        Args:
            n_samples: Number of synthetic samples to generate
        """
        print("Generating synthetic training data...")
        data = generate_synthetic_ml_data(n_samples)
        
        # Prepare features
        X = self.prepare_features(data)
        y = data['breach_occurred'].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        print("Training Random Forest model...")
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.3f}")
        
        self.is_trained = True
        
        # Save model
        self.save_model()
    
    def predict_breach_probability(
        self,
        lake_area: float,
        lake_volume: float,
        dam_type: str,
        rainfall_intensity: float,
        terrain_slope: float,
        temperature_anomaly: float
    ) -> float:
        """
        Predict breach probability for given lake conditions.
        
        Args:
            lake_area: Lake area in km²
            lake_volume: Lake volume in million m³
            dam_type: Type of dam (moraine, ice, bedrock)
            rainfall_intensity: Rainfall intensity in mm/day
            terrain_slope: Terrain slope in degrees
            temperature_anomaly: Temperature anomaly in °C
        
        Returns:
            Breach probability (0-1)
        """
        if not self.is_trained and self.model is None:
            self.train_model()
        
        # Create feature DataFrame
        features_df = pd.DataFrame({
            'lake_area': [lake_area],
            'lake_volume': [lake_volume],
            'dam_type': [dam_type],
            'rainfall_intensity': [rainfall_intensity],
            'terrain_slope': [terrain_slope],
            'temperature_anomaly': [temperature_anomaly]
        })
        
        # Prepare features
        X = self.prepare_features(features_df)
        
        # Predict probability
        prob = self.model.predict_proba(X)[0][1]
        
        return float(prob)
    
    def save_model(self):
        """Save trained model to disk."""
        if self.model is None:
            return
        
        # Ensure directory exists
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save model and encoder
        model_data = {
            'model': self.model,
            'label_encoder': self.label_encoder
        }
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Model saved to {self.model_path}")
    
    def load_model(self):
        """Load trained model from disk."""
        try:
            with open(self.model_path, 'rb') as f:
                model_data = pickle.load(f)
            
            self.model = model_data['model']
            self.label_encoder = model_data['label_encoder']
            self.is_trained = True
            
            print(f"Model loaded from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Training new model...")
            self.train_model()
