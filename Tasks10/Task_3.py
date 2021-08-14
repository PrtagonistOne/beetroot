class TVController:
    current_channel = 0

    def __init__(self, channels: list):
        self.channels = channels

    def first_channel(self) -> None:
        print(f'\tWELCOME TO CHANNEL #1\tYou are watching "{self.channels[0]}"')
        TVController.current_channel = 0
        input('Press any key to continue..')

    def last_channel(self) -> None:
        print(f'\tWELCOME TO CHANNEL #{len(self.channels)}\t You are watching "{self.channels[-1]}" ')
        TVController.current_channel = len(self.channels) - 1
        input('Press any key to continue..')

    def turn_channel(self, channel_number: int) -> None:
        try:
            print(f'\tWELCOME TO CHANNEL #{channel_number}\t You are watching "{self.channels[channel_number - 1]}" ')
            TVController.current_channel = channel_number-1
            input('Press any key to continue..')
        except IndexError:
            print('Channel does not exist, try again')

    def next_channel(self) -> None:
        if self.current_channel == len(self.channels) - 1:
            TVController.first_channel(self)
        else:
            TVController.current_channel += 1
            print(f'\tWELCOME TO CHANNEL #{self.current_channel+1}'
                  f'\tYou are watching "{self.channels[self.current_channel]}" ')
            input('Press any key to continue..')

    def previous_channel(self) -> None:
        if self.current_channel == 0:
            TVController.last_channel(self)
        else:
            TVController.current_channel -= 1
            print(f'\tWELCOME TO CHANNEL #{self.current_channel+1}'
                  f'\tYou are watching "{self.channels[self.current_channel]}" ')
            input('Press any key to continue..')

    def current(self) -> str:
        print(f'\tTHE CURRENT CHANNEL IS {self.channels[self.current_channel]}')
        return self.channels[self.current_channel]

    def is_exist(self, name) -> str:
        if name in self.channels:
            return 'Yes'
        else:
            return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000", "ICTV", "1+1", "2+2", "INTER"]
controller = TVController(CHANNELS)

remote = True
while remote:
    user_click = int(input('\tTV CONTROLLER 2000\nOptions:\n1. First channel\n2. Last channel\n3. Turn specific '
                           'channel\n4. Next channel\n5. Previous channel\n6. Current channel\n7. Is there a channel?'
                           '\nInput a number from 1 to 7: '))
    if user_click == 1:
        controller.first_channel()
    elif user_click == 2:
        controller.last_channel()
    elif user_click == 3:
        user_channel = int(input('Input a channel number: '))
        controller.turn_channel(user_channel)
    elif user_click == 4:
        controller.next_channel()
    elif user_click == 5:
        controller.previous_channel()
    elif user_click == 6:
        controller.current()
    elif user_click == 7:
        user_channel = input('Input a channel name or number to check if it is available: ')
        print(controller.is_exist(user_channel))
        input('Press a key to continue')
    else:
        continue
