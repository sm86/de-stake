import importlib

def main(blockchains):
    for blockchain in blockchains:
        # Dynamically import the module based on the blockchain name
        module_name = f'chains.{blockchain}'
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            print(f"Failed to import {module_name}")
            continue  # Skip to the next blockchain if import fails
        
        # Assume the class is named the same as the blockchain, but capitalized
        class_name = blockchain.capitalize()
        blockchain_class = getattr(module, class_name, None)
        if blockchain_class is None:
            print(f"Failed to find class {class_name} in {module_name}")
            continue  # Skip to the next blockchain if class is not found
        
        # Call the get_validators classmethod
        validators = blockchain_class.get_validators()
        if validators is not None:
            print(f'Validators for {blockchain}:')
            print(validators)
        else:
            print(f'Failed to retrieve validators for {blockchain}')

if __name__ == '__main__':
    # List of blockchain names
    blockchains = ['aptos', 'axelar', 'bnb', 'cosmos', 'osmosis', 'polygon', 'sui']  
    main(blockchains)