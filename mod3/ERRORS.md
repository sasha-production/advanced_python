# Correct code in person.py #
***
### Before: ###
    def get_age(self) -> int:</br>
        now: datetime.datetime = datetime.datetime.now()</br>
        return self.yob - now.year</br>
### After:</br> ###
    def get_age(self) -> int:</br>
        now: datetime.datetime = datetime.datetime.now()</br>
        return now.year - self.yob</br></br>
### Before: ###
    def set_name(self, name: str) -> None:
        self.name = self.name

### After: ###
    def set_name(self, name: str) -> None:
        self.name = name

### Before: ###
    def set_address(self, address: str) -> None:
        self.address == address

### After: ###
    def set_address(self, address: str) -> None:
        self.address = address
