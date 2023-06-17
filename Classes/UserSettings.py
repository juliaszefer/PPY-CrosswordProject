class UserSettings:
    def __init__(self, id_User, id_Color_bg=1, id_Color_outline=2, id_Color_font=2):
        self.id_User = id_User
        self.id_Color_bg = id_Color_bg
        self.id_Color_outline = id_Color_outline
        self.id_Color_font = id_Color_font

    def get_sql_data(self):
        data = (self.id_User, self.id_Color_bg, self.id_Color_outline, self.id_Color_font)
        return data
