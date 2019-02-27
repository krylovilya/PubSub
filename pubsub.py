class Bus:
    """
    Шина
    """

    def __init__(self):
        """
        room_dict - словарь, где ключ - имя комнаты, значение - лист подписчиков
        """
        self.room_dict = dict()

    def publish(self, room, publisher, msg):
        """
        Послать сообщение в комнату

        :param room: Имя комнаты
        :type room: str
        :param publisher: Экземпляр издателя
        :type publisher: Publisher
        :param msg: Данные
        :type msg: str
        """
        sub_list = self.room_dict.setdefault(room)
        if sub_list is not None:
            for sub in sub_list:
                sub.update(publisher.name, room, msg)

    def subscriber(self, room, subscriber):
        """
        Подписать подписчика к комнате

        :param room: Имя комнаты
        :type room: str
        :param subscriber: Экземпляр подписчика
        :type subscriber: Subscriber
        """
        room_sub_list = self.room_dict.get(room)
        if room_sub_list is None:
            print("[Bus] Room does not exist.")
            return
        room_sub_list.append(subscriber)

    def add_room(self, room):
        """
        Создать комнату

        :param room: Имя комнаты
        :type room: str
        """
        text_is_not_empty = room is not ""
        room_is_unique = self.room_dict.get(room, False) is False
        if text_is_not_empty and room_is_unique:
            self.room_dict.setdefault(room, [])
        else:
            print("[Bus] Error adding room!")


class Publisher:
    """
    Издатель
    """

    def __init__(self, name="nameless publisher"):
        """

        :param name: Имя издателя
        :type name: str
        """
        self.name = name

    def publish(self, bus, room, msg):
        """
        Послать сообщение в комнату

        :param bus: Экземпляр шины
        :type bus: Bus
        :param room: Имя комнаты
        :type room: str
        :param msg: Сообщение
        :type msg: str
        """
        bus.publish(room, self, msg)


class Subscriber:
    """
    Подписчик
    """

    def __init__(self, name="nameless subscriber"):
        """

        :param name: Имя подписчика
        :type name: str
        """
        self.name = name

    def subscriber(self, bus, room):
        """
        Подписаться на комнату

        :param bus: Шина
        :type bus: Bus
        :param room: Имя комнаты
        :type room: str
        """
        bus.subscriber(room, self)

    def get_msg(self, publisher_name, room, msg):
        """
        Приём и обработка полученного сообщения

        :param publisher_name: Имя издателя
        :type publisher_name: str
        :param room: Имя комнаты
        :type room: str
        :param msg: Сообщение
        :type msg: str
        """
        print("Subscriber {} room {} get a message: \"{}\" from the publisher {}".format(
            self.name, room, msg, publisher_name))
