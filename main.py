"""
Main Entry Point - Fantasy ARPG 3D Generator
"""

from terrain_generator.map_generator import TerrainGenerator
from character_monster_creator.character_builder import CharacterBuilder
from dungeon_generator.dungeon_builder import DungeonBuilder
from inventory_system.inventory import Inventory
from inventory_system.items import get_item

def main():
    print("=== Fantasy ARPG 3D Generator ===\n")
    
    # Generate terrain
    print("1. Generating terrain...")
    terrain_gen = TerrainGenerator(width=128, height=128, scale=30)
    heightmap = terrain_gen.generate_heightmap()
    terrain_gen.export_glb("terrain.glb", heightmap)
    
    # Create character
    print("2. Creating character...")
    hero = CharacterBuilder("Aragorn", "warrior")
    hero.export_glb("hero.glb")
    
    # Generate dungeon
    print("3. Generating dungeon...")
    dungeon = DungeonBuilder(width=15, height=15, num_rooms=8)
    dungeon.export_glb("dungeon.glb")
    
    # Setup inventory
    print("4. Setting up inventory...")
    inventory = Inventory(size=20)
    inventory.add_item(get_item("iron_sword"))
    inventory.add_item(get_item("health_potion"), 5)
    inventory.gold = 100
    
    print("\nGenerated items:")
    print(inventory.get_inventory_list())
    print(f"Gold: {inventory.gold}\n")
    
    print("=== Generation Complete ===")

if __name__ == "__main__":
    main()