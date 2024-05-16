# standardization_script.py
import os
from jinja2 import Environment, FileSystemLoader

def generate_file(template_name, output_path, context):
    template_dir = 'templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    rendered_content = template.render(context)
    with open(output_path, 'w') as f:
        f.write(rendered_content)

def generate_project(project_name, endpoints, tables):
    project_dir = project_name
    os.makedirs(project_dir, exist_ok=True)

    endpoint_logic_dir = os.path.join(project_dir, 'api')
    os.makedirs(endpoint_logic_dir, exist_ok=True)

    db_models_dir = os.path.join(project_dir, 'db')
    os.makedirs(db_models_dir, exist_ok=True)

    main_output_path = os.path.join(project_dir, 'main.py')
    context = {'endpoints': endpoints, 'tables': tables}
    generate_file('main_template.jinja2', main_output_path, context)

    for endpoint in endpoints:
        endpoint_logic_output_path = os.path.join(endpoint_logic_dir, f'{endpoint}.py')
        generate_file('endpoint_logic_template.jinja2', endpoint_logic_output_path, {})

    for table in tables:
        model_output_path = os.path.join(db_models_dir, f'{table}.py')
        generate_file('model_template.jinja2', model_output_path, {'table_name': table})

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    endpoints = input("Enter endpoints (comma-separated): ").split(',')
    tables = input("Enter table names (comma-separated): ").split(',')
    generate_project(project_name, endpoints, tables)
