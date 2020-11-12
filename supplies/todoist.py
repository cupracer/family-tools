import todoist
import re


class TodoistSync:

    api = None

    def __init__(self, api_key):
        self.api = todoist.TodoistAPI(api_key)
        self.api.sync()

    def get_item(self, project_id, section_id, name):
        project_data = self.api.projects.get_data(project_id)

        for item in project_data['items']:
            if item['section_id'] == section_id and item['content'].endswith(name):
                return item

    def add_to_shopping_list(self, project_id, section_id, name):
        item = self.get_item(project_id, section_id, name)
        counter = 1

        if item:
            m = re.search('^([0-9]+)x ' + name + '$', item['content'])
            print(m.group(1))
            counter = int(m.group(1))
            counter += 1
            name = str(counter) + 'x ' + name
            self.api.items.update(item['id'], content=name)
        else:
            name = str(counter) + 'x ' + name
            item = self.api.items.add(name, project_id=project_id)
            item.move(section_id=section_id)

        self.api.commit()
        return name