name	advapi32
type	win32

0000 stub AbortSystemShutdownA
0001 stub AbortSystemShutdownW
0002 stdcall AccessCheck(ptr long long ptr ptr ptr ptr ptr) AccessCheck32
0003 stub AccessCheckAndAuditAlarmA
0004 stub AccessCheckAndAuditAlarmW
0005 stub AddAccessAllowedAce
0006 stub AddAccessDeniedAce
0007 stub AddAce
0008 stub AddAuditAccessAce
0009 stub AdjustTokenGroups
0010 stdcall AdjustTokenPrivileges(long long ptr long ptr ptr) AdjustTokenPrivileges
0011 stdcall AllocateAndInitializeSid(ptr long long long long long long long long long ptr) AllocateAndInitializeSid
0012 stdcall AllocateLocallyUniqueId(ptr) AllocateLocallyUniqueId
0013 stub AreAllAccessesGranted
0014 stub AreAnyAccessesGranted
0015 stdcall BackupEventLogA (long str) BackupEventLog32A
0016 stdcall BackupEventLogW (long wstr) BackupEventLog32W
0017 stub ChangeServiceConfigA
0018 stub ChangeServiceConfigW
0019 stdcall ClearEventLogA (long str) ClearEventLog32A
0020 stdcall ClearEventLogW (long wstr) ClearEventLog32W
0021 stdcall CloseEventLog (long) CloseEventLog32
0022 stdcall CloseServiceHandle(long) CloseServiceHandle
0023 stdcall ControlService(long long ptr) ControlService
0024 stdcall CopySid(long ptr ptr) CopySid
0025 stub CreatePrivateObjectSecurity
0026 stub CreateProcessAsUserA
0027 stub CreateProcessAsUserW
0028 stdcall CreateServiceA(long ptr ptr long long long long ptr ptr ptr ptr ptr ptr) CreateService32A
0029 stdcall CreateServiceW (long ptr ptr long long long long ptr ptr ptr ptr ptr ptr) CreateService32A
0030 stdcall CryptAcquireContextA(ptr str str long long) CryptAcquireContextA
0031 stub CryptAcquireContextW
0032 stub CryptContextAddRef
0033 stub CryptCreateHash
0034 stub CryptDecrypt
0035 stub CryptDeriveKey
0036 stub CryptDestroyHash
0037 stub CryptDestroyKey
0038 stub CryptDuplicateKey
0039 stub CryptDuplicateHash
0040 stub CryptEncrypt
0041 stub CryptEnumProvidersA
0042 stub CryptEnumProvidersW
0043 stub CryptEnumProviderTypesA
0044 stub CryptEnumProviderTypesW
0045 stub CryptExportKey
0046 stub CryptGenKey
0047 stub CryptGetKeyParam
0048 stub CryptGetHashParam
0049 stub CryptGetProvParam
0050 stub CryptGenRandom
0051 stub CryptGetDefaultProviderA
0052 stub CryptGetDefaultProviderW
0053 stub CryptGetUserKey
0054 stub CryptHashData
0055 stub CryptHashSessionKey
0056 stub CryptImportKey
0057 stub CryptReleaseContext
0058 stub CryptSetHashParam
0059 stub CryptSetProvParam
0060 stub CryptSignHashA
0061 stub CryptSignHashW
0062 stub CryptSetProviderA
0063 stub CryptSetProviderW
0064 stub CryptSetProviderExA
0065 stub CryptSetProviderExW
0066 stub CryptVerifySignatureA
0067 stub CryptVerifySignatureW
0068 stub DeleteAce
0069 stdcall DeleteService(long) DeleteService
0070 stdcall DeregisterEventSource(long) DeregisterEventSource32
0071 stub DestroyPrivateObjectSecurity
0072 stub DuplicateToken
0073 stub EnumDependentServicesA
0074 stub EnumDependentServicesW
0075 stdcall EnumServicesStatusA (long long long ptr long ptr ptr ptr) EnumServicesStatus32A
0076 stdcall EnumServicesStatusW (long long long ptr long ptr ptr ptr) EnumServicesStatus32A
0077 stdcall EqualPrefixSid(ptr ptr) EqualPrefixSid
0078 stdcall EqualSid(ptr ptr) EqualSid
0079 stub FindFirstFreeAce
0080 stdcall FreeSid(ptr) FreeSid
0081 stub GetAce
0082 stub GetAclInformation
0083 stdcall GetFileSecurityA(str long ptr long ptr) GetFileSecurity32A
0084 stdcall GetFileSecurityW(wstr long ptr long ptr) GetFileSecurity32W
0085 stub GetKernelObjectSecurity
0086 stdcall GetLengthSid(ptr) GetLengthSid
0087 stdcall GetNumberOfEventLogRecords (long ptr) GetNumberOfEventLogRecords32
0088 stdcall GetOldestEventLogRecord (long ptr) GetOldestEventLogRecord32
0089 stub GetPrivateObjectSecurity
0090 stdcall GetSecurityDescriptorControl (ptr ptr ptr) GetSecurityDescriptorControl32
0091 stub GetSecurityDescriptorDacl
0092 stdcall GetSecurityDescriptorGroup(ptr ptr ptr) GetSecurityDescriptorGroup
0093 stdcall GetSecurityDescriptorLength(ptr) GetSecurityDescriptorLength
0094 stdcall GetSecurityDescriptorOwner(ptr ptr ptr) GetSecurityDescriptorOwner
0095 stub GetSecurityDescriptorSacl
0096 stub GetServiceDisplayNameA
0097 stub GetServiceDisplayNameW
0098 stub GetServiceKeyNameA
0099 stub GetServiceKeyNameW
0100 stdcall GetSidIdentifierAuthority(ptr) GetSidIdentifierAuthority
0101 stdcall GetSidLengthRequired(long) GetSidLengthRequired
0102 stdcall GetSidSubAuthority(ptr long) GetSidSubAuthority
0103 stdcall GetSidSubAuthorityCount(ptr) GetSidSubAuthorityCount
0104 stdcall GetTokenInformation(long long ptr long ptr) GetTokenInformation
0105 stdcall GetUserNameA(ptr ptr) GetUserName32A
0106 stdcall GetUserNameW(ptr ptr) GetUserName32W
0107 stub ImpersonateLoggedOnUser
0108 stub ImpersonateNamedPipeClient
0109 stdcall ImpersonateSelf(long) ImpersonateSelf32
0110 stub InitializeAcl
0111 stdcall InitializeSecurityDescriptor(ptr long) InitializeSecurityDescriptor
0112 stdcall InitializeSid(ptr ptr long) InitializeSid
0113 stub InitiateSystemShutdownA
0114 stub InitiateSystemShutdownW
0115 stdcall IsTextUnicode(ptr long ptr) RtlIsTextUnicode
0116 stub IsValidAcl
0117 stdcall IsValidSecurityDescriptor(ptr) IsValidSecurityDescriptor
0118 stdcall IsValidSid(ptr) IsValidSid
0119 stub LockServiceDatabase
0120 stub LogonUserA
0121 stub LogonUserW
0122 stub LookupAccountNameA
0123 stub LookupAccountNameW
0124 stdcall LookupAccountSidA(ptr ptr ptr ptr ptr ptr ptr) LookupAccountSid32A
0125 stdcall LookupAccountSidW(ptr ptr ptr ptr ptr ptr ptr) LookupAccountSid32W
0126 stub LookupPrivilegeDisplayNameA
0127 stub LookupPrivilegeDisplayNameW
0128 stub LookupPrivilegeNameA
0129 stub LookupPrivilegeNameW
0130 stdcall LookupPrivilegeValueA(ptr ptr ptr) LookupPrivilegeValue32A
0131 stdcall LookupPrivilegeValueW(ptr ptr ptr) LookupPrivilegeValue32W
0132 stub MakeAbsoluteSD
0133 stdcall MakeSelfRelativeSD(ptr ptr ptr) MakeSelfRelativeSD
0134 stub MapGenericMask
0135 stdcall NotifyBootConfigStatus(long) NotifyBootConfigStatus
0136 stdcall NotifyChangeEventLog (long long) NotifyChangeEventLog32
0137 stub ObjectCloseAuditAlarmA
0138 stub ObjectCloseAuditAlarmW
0139 stub ObjectOpenAuditAlarmA
0140 stub ObjectOpenAuditAlarmW
0141 stub ObjectPrivilegeAuditAlarmA
0142 stub ObjectPrivilegeAuditAlarmW
0143 stdcall OpenBackupEventLogA (str str) OpenBackupEventLog32A
0144 stdcall OpenBackupEventLogW (wstr wstr) OpenBackupEventLog32W
0145 stdcall OpenEventLogA (str str) OpenEventLog32A
0146 stdcall OpenEventLogW (wstr wstr) OpenEventLog32W
0147 stdcall OpenProcessToken(long long ptr) OpenProcessToken
0148 stdcall OpenSCManagerA(ptr ptr long) OpenSCManager32A
0149 stdcall OpenSCManagerW(ptr ptr long) OpenSCManager32W
0150 stdcall OpenServiceA(long str long) OpenService32A
0151 stdcall OpenServiceW(long wstr long) OpenService32W
0152 stdcall OpenThreadToken(long long long ptr) OpenThreadToken
0153 stub PrivilegeCheck
0154 stub PrivilegedServiceAuditAlarmA
0155 stub PrivilegedServiceAuditAlarmW
0156 stub QueryServiceConfigA
0157 stub QueryServiceConfigW
0158 stub QueryServiceLockStatusA
0159 stub QueryServiceLockStatusW
0160 stub QueryServiceObjectSecurity
0161 stdcall QueryServiceStatus(long ptr) QueryServiceStatus
0162 stdcall ReadEventLogA (long long long ptr long ptr ptr) ReadEventLog32A
0163 stdcall ReadEventLogW (long long long ptr long ptr ptr) ReadEventLog32W
0164 stdcall RegCloseKey(long) RegCloseKey
0165 stdcall RegConnectRegistryA(str long ptr) RegConnectRegistry32A
0166 stdcall RegConnectRegistryW(wstr long ptr) RegConnectRegistry32W
0167 stdcall RegCreateKeyA(long str ptr) RegCreateKey32A
0168 stdcall RegCreateKeyExA(long str long ptr long long ptr ptr ptr) RegCreateKeyEx32A
0169 stdcall RegCreateKeyExW(long wstr long ptr long long ptr ptr ptr) RegCreateKeyEx32W
0170 stdcall RegCreateKeyW(long wstr ptr) RegCreateKey32W
0171 stdcall RegDeleteKeyA(long str) RegDeleteKey32A
0172 stdcall RegDeleteKeyW(long wstr) RegDeleteKey32W
0173 stdcall RegDeleteValueA(long str) RegDeleteValue32A
0174 stdcall RegDeleteValueW(long wstr) RegDeleteValue32W
0175 stdcall RegEnumKeyA(long long ptr long) RegEnumKey32A
0176 stdcall RegEnumKeyExA(long long ptr ptr ptr ptr ptr ptr) RegEnumKeyEx32A
0177 stdcall RegEnumKeyExW(long long ptr ptr ptr ptr ptr ptr) RegEnumKeyEx32W
0178 stdcall RegEnumKeyW(long long ptr long) RegEnumKey32W
0179 stdcall RegEnumValueA(long long ptr ptr ptr ptr ptr ptr) RegEnumValue32A
0180 stdcall RegEnumValueW(long long ptr ptr ptr ptr ptr ptr) RegEnumValue32W
0181 stdcall RegFlushKey(long) RegFlushKey
0182 stdcall RegGetKeySecurity(long long ptr ptr) RegGetKeySecurity
0183 stdcall RegLoadKeyA(long str str) RegLoadKey32A
0184 stdcall RegLoadKeyW(long wstr wstr) RegLoadKey32W
0185 stdcall RegNotifyChangeKeyValue(long long long long long) RegNotifyChangeKeyValue
0186 stdcall RegOpenKeyA(long str ptr) RegOpenKey32A
0187 stdcall RegOpenKeyExA(long str long long ptr) RegOpenKeyEx32A
0188 stdcall RegOpenKeyExW(long wstr long long ptr) RegOpenKeyEx32W
0189 stdcall RegOpenKeyW(long wstr ptr) RegOpenKey32W
0190 stdcall RegQueryInfoKeyA(long ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) RegQueryInfoKey32A
0191 stdcall RegQueryInfoKeyW(long ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) RegQueryInfoKey32W
0192 stub RegQueryMultipleValuesA
0193 stub RegQueryMultipleValuesW
0194 stdcall RegQueryValueA(long str ptr ptr) RegQueryValue32A
0195 stdcall RegQueryValueExA(long str ptr ptr ptr ptr) RegQueryValueEx32A
0196 stdcall RegQueryValueExW(long wstr ptr ptr ptr ptr) RegQueryValueEx32W
0197 stdcall RegQueryValueW(long wstr ptr ptr) RegQueryValue32W
0198 stub RegRemapPreDefKey
0199 stdcall RegReplaceKeyA(long str str str) RegReplaceKey32A
0200 stdcall RegReplaceKeyW(long wstr wstr wstr) RegReplaceKey32W
0201 stdcall RegRestoreKeyA(long str long) RegRestoreKey32A
0202 stdcall RegRestoreKeyW(long wstr long) RegRestoreKey32W
0203 stdcall RegSaveKeyA(long ptr ptr) RegSaveKey32A
0204 stdcall RegSaveKeyW(long ptr ptr) RegSaveKey32W
0205 stdcall RegSetKeySecurity(long long ptr) RegSetKeySecurity
0206 stdcall RegSetValueA(long str long ptr long) RegSetValue32A
0207 stdcall RegSetValueExA(long str long long ptr long) RegSetValueEx32A
0208 stdcall RegSetValueExW(long wstr long long ptr long) RegSetValueEx32W
0209 stdcall RegSetValueW(long wstr long ptr long) RegSetValue32W
0210 stdcall RegUnLoadKeyA(long str) RegUnLoadKey32A
0211 stdcall RegUnLoadKeyW(long wstr) RegUnLoadKey32W
0212 stdcall RegisterEventSourceA(ptr ptr) RegisterEventSource32A
0213 stdcall RegisterEventSourceW(ptr ptr) RegisterEventSource32W
0214 stdcall RegisterServiceCtrlHandlerA (ptr ptr) RegisterServiceCtrlHandlerA
0215 stdcall RegisterServiceCtrlHandlerW (ptr ptr) RegisterServiceCtrlHandlerW
0216 stdcall ReportEventA (long long long long ptr long long str ptr) ReportEvent32A
0217 stdcall ReportEventW (long long long long ptr long long wstr ptr) ReportEvent32W
0218 stdcall RevertToSelf() RevertToSelf
0219 stub SetAclInformation
0220 stdcall SetFileSecurityA(str long ptr ) SetFileSecurity32A
0221 stdcall SetFileSecurityW(wstr long ptr) SetFileSecurity32W
0222 stub SetKernelObjectSecurity
0223 stub SetPrivateObjectSecurity
0224 stdcall SetSecurityDescriptorDacl(ptr long ptr long) RtlSetDaclSecurityDescriptor
0225 stub SetSecurityDescriptorGroup
0226 stub SetSecurityDescriptorOwner
0227 stub SetSecurityDescriptorSacl
0228 stub SetServiceBits
0229 stub SetServiceObjectSecurity
0230 stdcall SetServiceStatus(long long)SetServiceStatus
0231 stub SetThreadToken
0232 stub SetTokenInformation
0233 stdcall StartServiceA(long long ptr) StartService32A
0234 stdcall StartServiceCtrlDispatcherA(ptr) StartServiceCtrlDispatcher32A
0235 stdcall StartServiceCtrlDispatcherW(ptr) StartServiceCtrlDispatcher32W
0236 stdcall StartServiceW(long long ptr) StartService32W
0237 stub UnlockServiceDatabase
0238 stdcall LsaOpenPolicy(long long long long) LsaOpenPolicy
0239 stub LsaLookupSids
0240 stub LsaFreeMemory
0241 stub LsaQueryInformationPolicy
0242 stub LsaClose
0243 stub LsaSetInformationPolicy
0244 stub LsaLookupNames
0245 stub SystemFunction001
0246 stub SystemFunction002
0247 stub SystemFunction003
0248 stub SystemFunction004
0249 stub SystemFunction005
0250 stub SystemFunction006
0251 stub SystemFunction007
0252 stub SystemFunction008
0253 stub SystemFunction009
0254 stub SystemFunction010
0255 stub SystemFunction011
0256 stub SystemFunction012
0257 stub SystemFunction013
0258 stub SystemFunction014
0259 stub SystemFunction015
0260 stub SystemFunction016
0261 stub SystemFunction017
0262 stub SystemFunction018
0263 stub SystemFunction019
0264 stub SystemFunction020
0265 stub SystemFunction021
0266 stub SystemFunction022
0267 stub SystemFunction023
0268 stub SystemFunction024
0269 stub SystemFunction025
0270 stub SystemFunction026
0271 stub SystemFunction027
0272 stub SystemFunction028
0273 stub SystemFunction029
0274 stub SystemFunction030
0275 stub LsaQueryInfoTrustedDomain
0276 stub LsaQuerySecret
0277 stub LsaCreateSecret
0278 stub LsaOpenSecret
0279 stub LsaCreateTrustedDomain
0280 stub LsaOpenTrustedDomain
0281 stub LsaSetSecret
0282 stub LsaQuerySecret
0283 stub LsaCreateAccount
0284 stub LsaAddPrivilegesToAccount
0285 stub LsaRemovePrivilegesFromAccount
0286 stub LsaDelete
0287 stub LsaSetSystemAccessAccount
0288 stub LsaEnumeratePrivilegesOfAccount
0289 stub LsaEnumerateAccounts
0290 stub LsaOpenTrustedDomain
0291 stub LsaGetSystemAccessAccount
0292 stub LsaSetInformationTrustedDomain
0293 stub LsaEnumerateTrustedDomains
0294 stub LsaOpenAccount
0295 stub LsaEnumeratePrivileges
0296 stub LsaLookupPrivilegeDisplayName
0297 stub LsaICLookupNames
0298 stub ElfRegisterEventSourceW
0299 stub ElfReportEventW
0300 stub ElfDeregisterEventSource
0301 stub ElfDeregisterEventSourceW
0302 stub I_ScSetServiceBit
0303 stdcall SynchronizeWindows31FilesAndWindowsNTRegistry(long long long long) SynchronizeWindows31FilesAndWindowsNTRegistry
0304 stdcall QueryWindows31FilesMigration(long) QueryWindows31FilesMigration
0305 stub LsaICLookupSids
0306 stub SystemFunction031
0307 stub I_ScSetServiceBitsA
0308 stub EnumServiceGroupA
0309 stub EnumServiceGroupW
