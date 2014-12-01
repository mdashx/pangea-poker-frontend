# base_css = """
#     background: #616f91; /* Old browsers */
#     background-image:url('./avatar-default.png');
#     background-image:url('./avatar-default.png'), -moz-linear-gradient(45deg,  #616f91 0%, #bcbcbc 100%); /* FF3.6+ */
#     background-image:url('./avatar-default.png'), -webkit-gradient(linear, left bottom, right top, color-stop(0%,#616f91), color-stop(100%,#bcbcbc)); /* Chrome,Safari4+ */
#     background-image:url('./avatar-default.png'), -webkit-linear-gradient(45deg,  #616f91 0%,#bcbcbc 100%); /* Chrome10+,Safari5.1+ */
#     background-image:url('./avatar-default.png'), -o-linear-gradient(45deg,  #616f91 0%,#bcbcbc 100%); /* Opera 11.10+ */
#     background-image:url('./avatar-default.png'), -ms-linear-gradient(45deg,  #616f91 0%,#bcbcbc 100%); /* IE10+ */
#     background-image:url('./avatar-default.png'), linear-gradient(45deg,  #616f91 0%,#bcbcbc 100%); /* W3C */
# """


def seat_bg(avatar, color):
    base_css = [
        "background: #616f91; /* Old browsers */",
        "background-image:url('" + avatar + "');",
        "background-image:url('" + avatar + "'), -moz-linear-gradient(45deg,  " + color + " 0%, #bcbcbc 100%); /* FF3.6+ */",
        "background-image:url('" + avatar + "'), -webkit-gradient(linear, left bottom, right top, color-stop(0%," + color + "), color-stop(100%,#bcbcbc)); /* Chrome,Safari4+ */",
        "background-image:url('" + avatar + "'), -webkit-linear-gradient(45deg,  " + color + " 0%,#bcbcbc 100%); /* Chrome10+,Safari5.1+ */",
        "background-image:url('" + avatar + "'), -o-linear-gradient(45deg,  " + color + " 0%,#bcbcbc 100%); /* Opera 11.10+ */",
        "background-image:url('" + avatar + "'), -ms-linear-gradient(45deg,  " + color + " 0%,#bcbcbc 100%); /* IE10+ */",
        "background-image:url('" + avatar + "'), linear-gradient(45deg,  " + color + " 0%,#bcbcbc 100%); /* W3C */"]
    thiscss = ""
    for line in base_css:
        thiscss += line + "\n"
    return thiscss


css = ""

import settings as S
avatar = S.default_avatar
print avatar

seats = []
for i in range(9):
    seats.append({'num':i+1})

# import avatarcolors    
# colors = avatarcolors.black
# colors = avatarcolors.pink
# colors = avatarcolors.blue
# colors = avatarcolors.rainbow

colors = S.bgcolors

for seat in seats:
    css += "#seat-%s {\n" % (seat['num'])
    css += seat_bg(avatar, colors[seat['num']-1])
    css += "}\n"

with open("seat-gradients.css", 'w') as fh:
    fh.write(css)
