from allauth.socialaccount.providers.battlenet import validators

def username_validators():
    return [
            validators.BattletagUsernameValidator,
           ]