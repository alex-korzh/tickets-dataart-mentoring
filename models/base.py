from main import db


class ChangeableMixin:

    def update(self, data):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()