from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Ex.: João Silva'
            }
        )
    )
    senha_login=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Ex.: João Silva'
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Ex.: joaosilva@xpto.com'
            }
        )
    )

    senha_cadastro=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite sua senha'
            }
        )
    )

    senha_confirmar=forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder' : 'Digite sua senha mais uma vez'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo!!')
            else:
                return nome

    def clean_senha_confirmar(self):
         senha_1 = self.cleaned_data.get('senha_cadastro')
         senha_2 = self.cleaned_data.get('senha_confirmar')

         if senha_1 and senha_2:
              if senha_1 != senha_2:
                   raise forms.ValidationError('Senhas não conhecidem!!')
              else:
                  return senha_2