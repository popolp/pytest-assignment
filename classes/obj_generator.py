import names
from person import person


class object_generator:
    def __init__(self, object=person) -> None:
        if object is not person:
            raise ValueError("Types other than person are currently not supported")
        self.object = object

    def generate_x(self, num_of_objects=5):
        return [self.object(names.get_first_name()) for _ in range(num_of_objects)]


if __name__ == "__main__":
    o = object_generator(person)
    l = o.generate_x(5)
    for p in l:
        print(p.name)
