from abc import ABC, abstractmethod
from typing import Dict

class StarshipInformationColectorInterface(ABC):
    ''' Starship Information Colector Interface '''

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        ''' Must implement '''
        raise Exception('Must implement find_starship method')
