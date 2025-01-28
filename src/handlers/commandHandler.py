import os
import importlib

def loadCommandHandlers(bot):
    command_path = "src.commands"  
    base_dir = command_path.replace(".", "/")
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                relative_path = os.path.relpath(root, base_dir).replace("\\", ".").replace("/", ".")
                module_name = f"{command_path}{('.' + relative_path) if relative_path != '.' else ''}.{file[:-3]}"
                
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "setup"):
                        module.setup(bot)
                    print(f"Command Loaded: {module_name}")
                except Exception as e:
                    print(f"Error at loading {module_name}: {e}")
