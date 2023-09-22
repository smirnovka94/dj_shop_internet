from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        cleaned_list = ['Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция', 'Радар']
        if cleaned_data in cleaned_list:
            raise forms.ValidationError('Товар с таким наименованием запрещен')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        cleaned_list = ['Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция', 'Радар']
        if cleaned_data in cleaned_list:
            raise forms.ValidationError('Товар с таким описанием запрещен')

        return cleaned_data