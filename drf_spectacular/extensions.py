from abc import abstractmethod
from typing import List, Optional

from drf_spectacular.plumbing import OpenApiGeneratorExtension


class OpenApiAuthenticationExtension(OpenApiGeneratorExtension['OpenApiAuthenticationExtension']):
    _registry: List['OpenApiAuthenticationExtension'] = []

    name: str

    def get_security_requirement(self, auto_schema):
        assert self.name, 'name must be specified'
        return {self.name: []}

    @abstractmethod
    def get_security_definition(self, auto_schema):
        pass


class OpenApiSerializerExtension(OpenApiGeneratorExtension['OpenApiSerializerExtension']):
    _registry: List['OpenApiSerializerExtension'] = []

    def get_name(self) -> Optional[str]:
        """ return str for overriding default name extraction """
        return None

    @abstractmethod
    def map_serializer(self, auto_schema, direction):
        pass


class OpenApiSerializerFieldExtension(OpenApiGeneratorExtension['OpenApiSerializerFieldExtension']):
    _registry: List['OpenApiSerializerExtension'] = []

    @abstractmethod
    def map_serializer_field(self, auto_schema):
        pass
