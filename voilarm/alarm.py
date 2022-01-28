from datetime import datetime, timedelta
from threading import Timer


class Alarm:

    def __init__(self):
        self._timer = None
        self._dtalarm = None
        self._used = False

    def cancel_alarm(self):
        if self._timer == None:
            raise RuntimeError('The alarm is not scheduled')
        self._timer.cancel()

    def schedule(self, hour, minute, day=None, month=None, year=None):
        if self._used == True:
            raise RuntimeError('Alarms can only be scheduled once')
        dtnow = datetime.now()
        self._dtalarm = dtnow.replace(hour=hour, minute=minute,
                                      second=0, microsecond=0)
        if day != None:
            self._dtalarm.replace(day=day)
        if month != None:
            self._dtalarm.replace(month=month)
        if year != None:
            self._dtalarm.replace(year=year)
        if self._dtalarm <= dtnow:
            self._dtalarm += timedelta(days=1)

        delta_t = (self._dtalarm - dtnow).total_seconds()
        self._timer = Timer(delta_t, self._run)
        self._timer.start()
        print('The alarm will activate in ' + str(int(delta_t // 3600)) +
              ' hours, ' + str(int(delta_t // 60 % 60)) + ' minutes and ' + str(int(delta_t % 60)) + ' seconds.')
        self._used = True

    def _run(self):
        print('elo')
        self._timer = None
