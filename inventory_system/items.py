from enum import Enum
from dataclasses import dataclass
from typing import Dict

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    CONSUMABLE = "consumable"
    QUEST = "quest"
    MATERIAL = "material"
    SPELL_SCROLL = "spell_scroll"

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

@dataclass
class Item:
    name: str
    item_type: ItemType
    rarity: Rarity
    value: int
    weight: float
    description: str = ""
    quantity: int = 1
    
    # For weapons
    damage: int = 0
    
    # For armor
    defense: int = 0
    
    # For consumables
    hp_restore: int = 0
    mana_restore: int = 0
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "type": self.item_type.value,
            "rarity": self.rarity.name,
            "value": self.value,
            "weight": self.weight,
            "description": self.description,
            "quantity": self.quantity,
            "damage": self.damage,
            "defense": self.defense,
            "hp_restore": self.hp_restore,
            "mana_restore": self.mana_restore
        }

# Common items
ITEMS_DATABASE = {
    "iron_sword": Item(
        name="Iron Sword",
        item_type=ItemType.WEAPON,
        rarity=Rarity.COMMON,
        value=50,
        weight=3.0,
        description="A basic iron sword",
        damage=10
    ),
    "steel_armor": Item(
        name="Steel Armor",
        item_type=ItemType.ARMOR,
        rarity=Rarity.UNCOMMON,
        value=150,
        weight=15.0,
        description="Protective steel armor",
        defense=15
    ),
    "health_potion": Item(
        name="Health Potion",
        item_type=ItemType.CONSUMABLE,
        rarity=Rarity.COMMON,
        value=25,
        weight=0.5,
        description="Restores 50 HP",
        hp_restore=50
    ),
    "mana_potion": Item(
        name="Mana Potion",
        item_type=ItemType.CONSUMABLE,
        rarity=Rarity.COMMON,
        value=25,
        weight=0.5,
        description="Restores 50 Mana",
        mana_restore=50
    ),
    "gold_coin": Item(
        name="Gold Coin",
        item_type=ItemType.MATERIAL,
        rarity=Rarity.COMMON,
        value=1,
        weight=0.01,
        description="A gold coin",
        quantity=1
    ),
    "dragon_scale": Item(
        name="Dragon Scale",
        item_type=ItemType.MATERIAL,
        rarity=Rarity.LEGENDARY,
        value=500,
        weight=2.0,
        description="A legendary dragon scale",
        quantity=1
    ),
}