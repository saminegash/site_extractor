import os
import yaml


def update_yaml(filename):
    # Get the current directory
    current_directory = os.getcwd()

    # Find the first PDF file in the current directory
    pdf_file = None
    for file in os.listdir(current_directory):
        if file.endswith('.pdf'):
            pdf_file = file
            break

    if not pdf_file:
        raise FileNotFoundError("No PDF file found in the current directory")

    pdf_file_path = os.path.join(current_directory, pdf_file)

    # Read the YAML file
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)

    # Update the doc_search filename with the full path of the found PDF
    config['doc_search']['filename'] = pdf_file_path

    # Write the updated YAML file back
    with open(filename, 'w') as file:
        yaml.safe_dump(config, file)


# Specify your YAML file here
yaml_file = 'agent_config.yml'
update_yaml(yaml_file)
