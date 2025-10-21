from typing import Any, Generic, TypeVar

from api.common.response.response_code import CustomResponse, CustomResponseCode
from pydantic import BaseModel, Field

SchemaT = TypeVar("SchemaT")


class ResponseModel(BaseModel):
    """Response model without schema data.

    When you want to return a response without schema data, you can use this model.
    """

    code: int = Field(
        default=CustomResponseCode.HTTP_200.code, description="Response code"
    )
    msg: str = Field(
        default=CustomResponseCode.HTTP_200.message, description="Response message"
    )
    data: Any | None = Field(default=None, description="Response data")


class ResponseSchemaModel(ResponseModel, Generic[SchemaT]):
    """Response model with schema data.

    When you want to return a response with schema data, you can use this model.
    """

    data: SchemaT = Field(default=None, description="Response data")


class ResponseBase:
    @staticmethod
    def _response(
        *,
        response: CustomResponseCode | CustomResponse,
        data: Any | None,
    ) -> ResponseModel | ResponseSchemaModel:
        return ResponseModel(code=response.code, msg=response.msg, data=data)

    def success(
        self,
        *,
        response: CustomResponseCode = CustomResponseCode.HTTP_200,
        data: Any | None = None,
    ) -> ResponseModel | ResponseSchemaModel:
        return self._response(response=response, data=data)

    def error(
        self,
        *,
        response: CustomResponseCode = CustomResponseCode.HTTP_400,
        data: Any | None = None,
    ) -> ResponseModel | ResponseSchemaModel:
        return self._response(response=response, data=data)


response_base: ResponseBase = ResponseBase()
