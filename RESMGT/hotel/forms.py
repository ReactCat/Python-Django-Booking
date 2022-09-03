from django import forms

class AvailabilityForm(forms.Form):

    ROOM_CATEGORIES=(
        ('AC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')
    check_out = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')

    