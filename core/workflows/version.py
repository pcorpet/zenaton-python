import abc

from core.abstracts.workflow import Workflow
from core.exceptions import ExternalError


# from core.traits.zenatonable import Zenatonable


class Version(Zenatonable):

    def __init__(self, *args):
        self.args = args

    @abc.abstractmethod
    def versions(self):
        raise NotImplementedError("Please override the `versions' method in your subclass")

    """Calls handle on the current implementation"""

    def handle(self):
        self.current_implementation.handle

    """
    Get the current implementation class
    returns class
    """

    def current(self):
        return self.__get_versions[-1]

    """
        Get the first implementation class
        returns class
    """

    def initial(self):
        return self.__get_versions[0]

    """
    Returns an instance of the current implementation
    :returns core.abstracts.workflow.Workflow
    """

    def current_implementation(self):
        self.current(self.args)

    def __get_versions(self):
        if not type(self.versions()) == list:
            raise ExternalError
        if not len(self.versions()) > 0:
            raise ExternalError
        for version in self.versions():
            if not issubclass(type(version), Workflow):
                raise ExternalError
