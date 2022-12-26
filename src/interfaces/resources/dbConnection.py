# Implementa la abstracción de la conexion a la db
from abc import ABC
from abc import abstractmethod
import pandas as pd

class IDBConnection(ABC): 
    @abstractmethod
    def db_connection(query, sp_type) -> pd.DataFrame:
        """Get ods connection"""