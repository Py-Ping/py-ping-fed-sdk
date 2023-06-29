from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import EmailVerificationType


class EmailVerificationConfig(Model):
    """A local identity email verification configuration.

    Attributes
    ----------
    emailVerificationEnabled: bool
        Whether the email ownership verification is enabled.

    verifyEmailTemplateName: str
        The template name for verify email. The default is message-template-email-ownership-verification.html.

    emailVerificationSentTemplateName: str
        The template name for email verification sent. The default is local.identity.email.verification.sent.html.
        Note:Only applicable if EmailVerificationType is OTL.

    emailVerificationSuccessTemplateName: str
        The template name for email verification success. The default is local.identity.email.verification.success.html.

    emailVerificationErrorTemplateName: str
        The template name for email verification error.  The default is local.identity.email.verification.error.html.

    emailVerificationType: EmailVerificationType
        Email Verification Type.

    otpLength: int
        The OTP length generated for email verification. The default is 8.
        Note: Only applicable if EmailVerificationType is OTP.

    otpRetryAttempts: int
        The number of OTP retry attempts for email verification. The default is 3.
        Note: Only applicable if EmailVerificationType is OTP.

    allowedOtpCharacterSet: str
        The allowed character set used to generate the OTP. The default is 23456789BCDFGHJKMNPQRSTVWXZbcdfghjkmnpqrstvwxz.
        Note: Only applicable if EmailVerificationType is OTP.

    otpTimeToLive: int
        Field used OTP time to live. The default is 15.
        Note: Only applicable if EmailVerificationType is OTP.

    emailVerificationOtpTemplateName: str
        The template name for email verification OTP verification.  The default is local.identity.email.verification.otp.html.
        Note: Only applicable if EmailVerificationType is OTP.

    otlTimeToLive: int
        Field used OTL time to live. The default is 1440.
        Note: Only applicable if EmailVerificationType is OTL.

    fieldForEmailToVerify: str
        Field used for email ownership verification.
        Note: Not required when emailVerificationEnabled is set to false.

    fieldStoringVerificationStatus: str
        Field used for storing email verification status.
        Note: Not required when emailVerificationEnabled is set to false.

    notificationPublisherRef: ResourceLink
        Reference to the associated notification publisher.

    requireVerifiedEmail: bool
        Whether the user must verify their email address before they can complete a single sign-on transaction. The default is false.

    requireVerifiedEmailTemplateName: str
        The template to render when the user must verify their email address before they can complete a single sign-on transaction. The default is local.identity.email.verification.required.html.
        Note:Only applicable if EmailVerificationType is OTL and requireVerifiedEmail is true.

    """

    def __init__(self, fieldForEmailToVerify: str, fieldStoringVerificationStatus: str, emailVerificationEnabled: bool = None, verifyEmailTemplateName: str = None, emailVerificationSentTemplateName: str = None, emailVerificationSuccessTemplateName: str = None, emailVerificationErrorTemplateName: str = None, emailVerificationType: EmailVerificationType = None, otpLength: int = None, otpRetryAttempts: int = None, allowedOtpCharacterSet: str = None, otpTimeToLive: int = None, emailVerificationOtpTemplateName: str = None, otlTimeToLive: int = None, notificationPublisherRef: ResourceLink = None, requireVerifiedEmail: bool = None, requireVerifiedEmailTemplateName: str = None) -> None:
        self.emailVerificationEnabled = emailVerificationEnabled
        self.verifyEmailTemplateName = verifyEmailTemplateName
        self.emailVerificationSentTemplateName = emailVerificationSentTemplateName
        self.emailVerificationSuccessTemplateName = emailVerificationSuccessTemplateName
        self.emailVerificationErrorTemplateName = emailVerificationErrorTemplateName
        self.emailVerificationType = emailVerificationType
        self.otpLength = otpLength
        self.otpRetryAttempts = otpRetryAttempts
        self.allowedOtpCharacterSet = allowedOtpCharacterSet
        self.otpTimeToLive = otpTimeToLive
        self.emailVerificationOtpTemplateName = emailVerificationOtpTemplateName
        self.otlTimeToLive = otlTimeToLive
        self.fieldForEmailToVerify = fieldForEmailToVerify
        self.fieldStoringVerificationStatus = fieldStoringVerificationStatus
        self.notificationPublisherRef = notificationPublisherRef
        self.requireVerifiedEmail = requireVerifiedEmail
        self.requireVerifiedEmailTemplateName = requireVerifiedEmailTemplateName

    def _validate(self) -> bool:
        return any(x for x in ["fieldForEmailToVerify", "fieldStoringVerificationStatus"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EmailVerificationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.emailVerificationEnabled, self.verifyEmailTemplateName, self.emailVerificationSentTemplateName, self.emailVerificationSuccessTemplateName, self.emailVerificationErrorTemplateName, self.emailVerificationType, self.otpLength, self.otpRetryAttempts, self.allowedOtpCharacterSet, self.otpTimeToLive, self.emailVerificationOtpTemplateName, self.otlTimeToLive, self.fieldForEmailToVerify, self.fieldStoringVerificationStatus, self.notificationPublisherRef, self.requireVerifiedEmail, self.requireVerifiedEmailTemplateName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["emailVerificationEnabled", "verifyEmailTemplateName", "emailVerificationSentTemplateName", "emailVerificationSuccessTemplateName", "emailVerificationErrorTemplateName", "emailVerificationType", "otpLength", "otpRetryAttempts", "allowedOtpCharacterSet", "otpTimeToLive", "emailVerificationOtpTemplateName", "otlTimeToLive", "fieldForEmailToVerify", "fieldStoringVerificationStatus", "notificationPublisherRef", "requireVerifiedEmail", "requireVerifiedEmailTemplateName"] and v is not None:
                if k == "emailVerificationEnabled":
                    valid_data[k] = bool(v)
                if k == "verifyEmailTemplateName":
                    valid_data[k] = str(v)
                if k == "emailVerificationSentTemplateName":
                    valid_data[k] = str(v)
                if k == "emailVerificationSuccessTemplateName":
                    valid_data[k] = str(v)
                if k == "emailVerificationErrorTemplateName":
                    valid_data[k] = str(v)
                if k == "emailVerificationType":
                    valid_data[k] = EmailVerificationType[v]
                if k == "otpLength":
                    valid_data[k] = int(v)
                if k == "otpRetryAttempts":
                    valid_data[k] = int(v)
                if k == "allowedOtpCharacterSet":
                    valid_data[k] = str(v)
                if k == "otpTimeToLive":
                    valid_data[k] = int(v)
                if k == "emailVerificationOtpTemplateName":
                    valid_data[k] = str(v)
                if k == "otlTimeToLive":
                    valid_data[k] = int(v)
                if k == "fieldForEmailToVerify":
                    valid_data[k] = str(v)
                if k == "fieldStoringVerificationStatus":
                    valid_data[k] = str(v)
                if k == "notificationPublisherRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "requireVerifiedEmail":
                    valid_data[k] = bool(v)
                if k == "requireVerifiedEmailTemplateName":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["emailVerificationEnabled", "verifyEmailTemplateName", "emailVerificationSentTemplateName", "emailVerificationSuccessTemplateName", "emailVerificationErrorTemplateName", "emailVerificationType", "otpLength", "otpRetryAttempts", "allowedOtpCharacterSet", "otpTimeToLive", "emailVerificationOtpTemplateName", "otlTimeToLive", "fieldForEmailToVerify", "fieldStoringVerificationStatus", "notificationPublisherRef", "requireVerifiedEmail", "requireVerifiedEmailTemplateName"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
