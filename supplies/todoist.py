import todoist
import re


class TodoistSync:

    api = None

    def __init__(self, api_key):
        self.api = todoist.TodoistAPI(api_key)
        self.api.sync()

    def get_project_id(self, project_name):
        for project in self.api.state['projects']:
            if project['name'] == project_name:
                return project['id']

    def get_section_id(self, project_id, section_name):
        for section in self.api.state['sections']:
            if section['project_id'] == project_id and section['name'] == section_name:
                return section['id']

    def get_item(self, project_id, section_id, name):
        project_data = self.api.projects.get_data(project_id)

        for item in project_data['items']:
            if item['section_id'] == section_id and item['content'].endswith(name):
                return item

    def add_to_shopping_list(self, project_name, section_name, supply_name):
        project_id = self.get_project_id(project_name)
        section_id = self.get_section_id(project_id, section_name)
        item = self.get_item(project_id, section_id, supply_name)
        counter = 1

        if item:
            supply_name_escaped = str.replace(supply_name, '(', '\\(').replace(')', '\\)')
            m = re.search('^([0-9]+)x ' + supply_name_escaped + '$', item['content'])

            print(m.group(1))
            counter = int(m.group(1))
            counter += 1
            name = str(counter) + 'x ' + supply_name
            self.api.items.update(item['id'], content=name)
        else:
            name = str(counter) + 'x ' + supply_name
            item = self.api.items.add(name, project_id=project_id)
            item.move(section_id=section_id)

        self.api.commit()
        return name
