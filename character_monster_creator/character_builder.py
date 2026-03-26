class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.stats = self.initialize_stats()
        self.equipment = []

    def initialize_stats(self):
        # Customize initial stats for different classes
        if self.character_class == 'Warrior':
            return {'strength': 15, 'agility': 5, 'intelligence': 3}
        elif self.character_class == 'Mage':
            return {'strength': 3, 'agility': 7, 'intelligence': 15}
        elif self.character_class == 'Rogue':
            return {'strength': 5, 'agility': 15, 'intelligence': 7}
        elif self.character_class == 'Paladin':
            return {'strength': 10, 'agility': 10, 'intelligence': 5}
        else:
            raise ValueError('Unknown character class')

    def equip(self, item):
        self.equipment.append(item)

    def get_character_info(self):
        return {"name": self.name, "class": self.character_class, "stats": self.stats, "equipment": self.equipment}


class Equipment:
    def __init__(self, name, equipment_type):
        self.name = name
        self.equipment_type = equipment_type


class ModelGenerator:
    @staticmethod
    def generate_3d_model(character):
        # Placeholder for model generation logic
        return f"3D model for {character.name} the {character.character_class} generated."


# Example Usage:
if __name__ == '__main__':
    hero = Character(name='Arthas', character_class='Paladin')
    sword = Equipment(name='Excalibur', equipment_type='Weapon')
    hero.equip(sword)
    print(hero.get_character_info())
    print(ModelGenerator.generate_3d_model(hero))