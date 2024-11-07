from typing import Annotated
from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import thirdparty, session, dashboard
from supertokens_python.recipe.thirdparty.provider import ProviderInput, ProviderConfig, ProviderClientConfig
from fastapi import Depends
from functools import lru_cache

from config import Settings


@lru_cache
def get_settings():
    return Settings()


def supertokens_init(settings: Annotated[Settings, Depends(get_settings)]):
    print(settings)
    init(
        app_info=InputAppInfo(
            app_name=settings.app_name,
            api_domain=settings.api_domain,
            website_domain=settings.website_domain,
            api_base_path=settings.api_base_path,
            website_base_path=settings.website_base_path
        ),
        supertokens_config=SupertokensConfig(
            connection_uri=settings.supertokens_connection_uri
        ),
        framework='fastapi',
        recipe_list=[
            session.init(),  # initializes session features
            dashboard.init(),
            thirdparty.init(
                sign_in_and_up_feature=thirdparty.SignInAndUpFeature(providers=[
                    # We have provided you with development keys which you can use for testing.
                    # IMPORTANT: Please replace them with your own OAuth keys for production use.
                    ProviderInput(
                        config=ProviderConfig(
                            third_party_id="google",
                            clients=[
                                ProviderClientConfig(
                                    client_id="1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com",
                                    client_secret="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",
                                ),
                            ],
                        ),
                    ),
                    ProviderInput(
                        config=ProviderConfig(
                            third_party_id="github",
                            clients=[
                                ProviderClientConfig(
                                    client_id="467101b197249757c71f",
                                    client_secret="e97051221f4b6426e8fe8d51486396703012f5bd",
                                )
                            ],
                        ),
                    ),
                    ProviderInput(
                        config=ProviderConfig(
                            third_party_id="apple",
                            clients=[
                                ProviderClientConfig(
                                    client_id="io.supertokens.example.service",
                                    additional_config={
                                        "keyId": "7M48Y4RYDL",
                                        "privateKey": "-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgu8gXs+XYkqXD6Ala9Sf/iJXzhbwcoG5dMh1OonpdJUmgCgYIKoZIzj0DAQehRANCAASfrvlFbFCYqn3I2zeknYXLwtH30JuOKestDbSfZYxZNMqhF/OzdZFTV0zc5u5s3eN+oCWbnvl0hM+9IW0UlkdA\n-----END PRIVATE KEY-----",
                                        "teamId": "YWQCXGJRJL"
                                    },
                                ),
                            ],
                        ),
                    ),
                ])
            )
        ],
        mode='asgi'  # use wsgi if you are running using gunicorn
    )
