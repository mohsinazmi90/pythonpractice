def make_coffee(water, coffee_powder, milk=None, sugar=None):
    # Step 1: Boil the water
    print("\nBoiling water...\n")
    
    # Step 2: Add coffee powder to the cup
    print(f"Adding {coffee_powder} of coffee powder to the cup...")
    
    # Step 3: Pour the hot water into the cup
    print("Pouring hot water into the cup...\n")
    
    # Step 4: Stir the coffee
    print("Stirring the coffee...\n")
    
    # Step 5: Optional - Add milk if provided
    if milk:
        print(f"Adding {milk} of milk to the coffee...")
        print("Stirring the coffee with milk...")
    
    # Step 6: Optional - Add sugar if provided
    if sugar:
        print(f"Adding {sugar} of sugar to the coffee...")
        print("Stirring the coffee with sugar...\n")
    
    # Final step: The coffee is ready
    print("\nYour cup of instant coffee is ready! Enjoy!\n")    
    
if __name__ == "__main__":
    make_coffee(water=200, coffee_powder=2, milk=50)