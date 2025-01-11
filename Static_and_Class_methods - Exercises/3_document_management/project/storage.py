from typing import Union

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        self.__add_element(category, self.categories)

    def add_topic(self, topic: Topic):
        self.__add_element(topic, self.topics)

    def add_document(self, document: Document):
        self.__add_element(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        category = self.__get_object(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_object(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_object(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__get_object(document_id, self.documents)

    @staticmethod
    def __get_object(uid, collection: list):
        obj = next((obj for obj in collection if obj.id == uid), None)
        return obj

    @staticmethod
    def __add_element(obj, collection: list[Union[Category, Topic, Document]]):
        if obj not in collection:
            collection.append(obj)

    def __edit(self, obj_id, collection: list[Union[Category, Topic, Document]], *args):
        obj = self.__get_object(obj_id, collection)
        if obj:
            return obj.edit(*args)

    def __repr__(self):
        result = [repr(d) for d in self.documents]
        return "\n".join(result)