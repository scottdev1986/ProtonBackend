import pytest
from unittest.mock import patch, MagicMock
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import status

import jwt

from app.utils.auth import VerifyToken, UnauthorizedException, UnauthenticatedException


@pytest.fixture
def verifier():
    return VerifyToken()


@pytest.mark.asyncio
async def test_verify_missing_token(verifier):
    with pytest.raises(UnauthenticatedException) as exc_info:
        await verifier.verify(security_scopes=MagicMock(), token=None)

    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Requires authentication" in exc_info.value.detail


@patch("jwt.PyJWKClient.get_signing_key_from_jwt")
@pytest.mark.asyncio
async def test_verify_invalid_token(mock_jwk, verifier):
    mock_jwk.side_effect = jwt.exceptions.DecodeError("Invalid token format")

    fake_token_credentials = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials="fake-invalid-token"
    )

    with pytest.raises(UnauthorizedException) as exc_info:
        await verifier.verify(security_scopes=MagicMock(), token=fake_token_credentials)

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
    assert "Invalid token format" in exc_info.value.detail


@patch("jwt.PyJWKClient.get_signing_key_from_jwt")
@patch("jwt.decode")
@pytest.mark.asyncio
async def test_verify_valid_token(mock_decode, mock_jwk, verifier):
    mock_signing_key = MagicMock()
    mock_jwk.return_value.key = mock_signing_key

    mock_payload = {"sub": "1234567890", "name": "Jane Doe", "iat": 1516239022}
    mock_decode.return_value = mock_payload

    fake_token_credentials = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials="fake-valid-token"
    )

    returned_payload = await verifier.verify(
        security_scopes=MagicMock(),
        token=fake_token_credentials,
    )
    assert returned_payload == mock_payload

    mock_decode.assert_called_once_with(
        "fake-valid-token",
        mock_signing_key,
        algorithms=verifier.config.auth0_algorithms,
        audience=verifier.config.auth0_api_audience,
        issuer=verifier.config.auth0_issuer,
    )
