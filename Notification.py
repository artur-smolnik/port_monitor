import DiffAnalyser
from pynotifier import Notification


class Alert:

    def show(self, scan_type, ports):
        notification_text = ''
        if scan_type == -1:
            pass
            # print("There are no any changes.")
        elif scan_type == 0:
            for port in ports:
                notification_text += port
                if ports.index(port) != len(ports) - 1:
                    notification_text += ', '

            Notification(
                title='MapDiff Port Scanner',
                description='Some ports are closed:' + notification_text,
                icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
                duration=3,  # Duration in seconds
                urgency=Notification.URGENCY_CRITICAL
            ).send()

        elif scan_type == 1:
            # print("Some new ports are opened: ", end='')
            for port in ports:
                notification_text += port
                if ports.index(port) != len(ports) - 1:
                    notification_text += ', '

            Notification(
                title='MapDiff Port Scanner',
                description='New ports are open: '+ notification_text,
                icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
                duration=3,  # Duration in seconds
                urgency=Notification.URGENCY_CRITICAL
            ).send()

