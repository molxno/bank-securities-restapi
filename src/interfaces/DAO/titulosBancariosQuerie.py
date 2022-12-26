# Implementa la abstracción de la clase
from abc import ABC
from abc import abstractmethod
import pandas as pd

class QueriesDAO(ABC): 
    @abstractmethod
    def get_titulos_bancarios() -> pd.DataFrame:
        """Get all titulos bancarios"""

    def get_titulo_bancario() -> pd.DataFrame:
        """Get titulo bancario"""

    def post_titulo_bancario() -> pd.DataFrame:
        """Post titulo bancario"""

    def patch_paga_titulo_bancario() -> pd.DataFrame:
        """Patch titulo bancario"""

    def delete_titulo_bancario() -> pd.DataFrame:
        """Delete titulo bancario"""