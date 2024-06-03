class Student():
    def __init__(self, name, class_room, scores):
        self.name = name
        self.class_room = class_room
        self.scores = scores
        self.average_score = sum(scores.values()) / len(scores)
    
    def obj_to_dict(self):
        return {
            'Name' : self.name,
            'Class Room' : self.class_room,
            'Scores' : self.scores,
            'Average Score' : self.average_score
        }
    
    def dict_to_obj(self):
        return Student(
            name = self['Name'],
            class_room = self['Class Room'],
            scores = self['Scores']
        )