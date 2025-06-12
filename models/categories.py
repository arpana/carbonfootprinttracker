from dataclasses import dataclass

@dataclass
class Category:
    id: int
    name: str
    description: str
    emission_factor: float  # Emission factor in kg CO2e per unit

    def calculate_emissions(self, quantity: float) -> float:
        """
        Calculate the carbon emissions for a given quantity of this category.

        :param quantity: The quantity of the category item.
        :return: The calculated emissions in kg CO2e.
        """
        return self.emission_factor * quantity