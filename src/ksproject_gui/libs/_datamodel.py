# Processing root key: KivySchoolData
from pathlib import Path

class KivySchoolData:

    class Android:
        
        package_name: str
        
        archs: list[str]
        
        api: int | None
        
        api_min: int | None
        
        sdk: str | None
        
        ndk: str | None
        
        ndk_api: int | None
        
        sdk_path: Path | None
        
        ndk_path: Path | None
        
        java_path: Path | None
        
        global_tools: bool
        
        global_tools_path: Path | None
        
        icon: Path | None
        
        presplash: Path | None
        
        presplash_color: str | None
        
        presplash_lottie: Path | None
        
        meta_data: dict[str, str]
        
        permissions: list[str]
        
        gradle_dependencies: list[str]
        
        services: list["ServiceData"]
        
        version_code: int | None
        
        version_name: str | None

        def __init__(self, data: dict):
            self.package_name = str(data.get("package_name"))
            self.archs = list(data.get("archs"))
            self.api = int(data.get("api")) if "api" in data else None
            self.api_min = int(data.get("api_min")) if "api_min" in data else None
            self.sdk = str(data.get("sdk")) if "sdk" in data else None
            self.ndk = str(data.get("ndk")) if "ndk" in data else None
            self.ndk_api = int(data.get("ndk_api")) if "ndk_api" in data else None
            self.sdk_path = Path(data.get("sdk_path")) if "sdk_path" in data else None
            self.ndk_path = Path(data.get("ndk_path")) if "ndk_path" in data else None
            self.java_path = Path(data.get("java_path")) if "java_path" in data else None
            self.global_tools = bool(data.get("global_tools"))
            self.global_tools_path = Path(data.get("global_tools_path")) if "global_tools_path" in data else None
            self.icon = Path(data.get("icon")) if "icon" in data else None
            self.presplash = Path(data.get("presplash")) if "presplash" in data else None
            self.presplash_color = str(data.get("presplash_color")) if "presplash_color" in data else None
            self.presplash_lottie = Path(data.get("presplash_lottie")) if "presplash_lottie" in data else None
            self.meta_data = dict(data.get("meta_data"))
            self.permissions = list(data.get("permissions"))
            self.gradle_dependencies = list(data.get("gradle_dependencies"))
            self.services = list(data.get("services"))
            self.version_code = int(data.get("version_code")) if "version_code" in data else None
            self.version_name = str(data.get("version_name")) if "version_name" in data else None

    class IOS:
        
        bundle_id: str
        
        info_plist: dict[str, object] | None
        
        entitlements: dict[str, object] | None
        
        permissions: list[str] | None
        
        frameworks: list[str] | None
        
        site_frameworks: list[str] | None
        
        developer_team: str | None

        def __init__(self, data: dict):
            self.bundle_id = str(data.get("bundle_id"))
            self.info_plist = dict[str, object](data.get("info_plist")) if "info_plist" in data else None
            self.entitlements = dict[str, object](data.get("entitlements")) if "entitlements" in data else None
            self.permissions = list[str](data.get("permissions")) if "permissions" in data else None
            self.frameworks = list[str](data.get("frameworks")) if "frameworks" in data else None
            self.site_frameworks = list[str](data.get("site_frameworks")) if "site_frameworks" in data else None
            self.developer_team = str(data.get("developer_team")) if "developer_team" in data else None

    class MacOS:
        
        bundle_id: str
        
        info_plist: dict[str, object] | None
        
        entitlements: dict[str, object] | None
        
        permissions: list[str] | None
        
        frameworks: list[str] | None
        
        site_frameworks: list[str] | None
        
        developer_team: str | None
        
        app_category: str | None
        
        app_subcategory: str | None

        def __init__(self, data: dict):
            self.bundle_id = str(data.get("bundle_id"))
            self.info_plist = dict[str, object](data.get("info_plist")) if "info_plist" in data else None
            self.entitlements = dict[str, object](data.get("entitlements")) if "entitlements" in data else None
            self.permissions = list[str](data.get("permissions")) if "permissions" in data else None
            self.frameworks = list[str](data.get("frameworks")) if "frameworks" in data else None
            self.site_frameworks = list[str](data.get("site_frameworks")) if "site_frameworks" in data else None
            self.developer_team = str(data.get("developer_team")) if "developer_team" in data else None
            self.app_category = str(data.get("app_category")) if "app_category" in data else None
            self.app_subcategory = str(data.get("app_subcategory")) if "app_subcategory" in data else None


# Processing root key: KivySchoolData
from pathlib import Path
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty, BooleanProperty, DictProperty
from kivy.event import EventDispatcher

class KivySchoolData(EventDispatcher):

    class Android(EventDispatcher):
        
        package_name = StringProperty()
        
        archs = ListProperty() # type: ListProperty[str]
        
        api = NumericProperty() # type: int | None
        
        api_min = NumericProperty() # type: int | None
        
        sdk = StringProperty()
        
        ndk = StringProperty()
        
        ndk_api = NumericProperty() # type: int | None
        
        sdk_path = StringProperty()
        
        ndk_path = StringProperty()
        
        java_path = StringProperty()
        
        global_tools = BooleanProperty() # type: bool
        
        global_tools_path = StringProperty()
        
        icon = StringProperty()
        
        presplash = StringProperty()
        
        presplash_color = StringProperty()
        
        presplash_lottie = StringProperty()
        
        meta_data = DictProperty() # type: dict[str, str]
        
        permissions = ListProperty() # type: ListProperty[str]
        
        gradle_dependencies = ListProperty() # type: ListProperty[str]
        
        services = ListProperty() # type: ListProperty[ServiceData]
        
        version_code = NumericProperty() # type: int | None
        
        version_name = StringProperty()

        def __init__(self, data: dict):
            self.package_name = str(data.get("package_name"))
            self.archs = list(data.get("archs"))
            self.api = int(data.get("api")) if "api" in data else None
            self.api_min = int(data.get("api_min")) if "api_min" in data else None
            self.sdk = str(data.get("sdk")) if "sdk" in data else None
            self.ndk = str(data.get("ndk")) if "ndk" in data else None
            self.ndk_api = int(data.get("ndk_api")) if "ndk_api" in data else None
            self.sdk_path = Path(data.get("sdk_path")) if "sdk_path" in data else None
            self.ndk_path = Path(data.get("ndk_path")) if "ndk_path" in data else None
            self.java_path = Path(data.get("java_path")) if "java_path" in data else None
            self.global_tools = bool(data.get("global_tools"))
            self.global_tools_path = Path(data.get("global_tools_path")) if "global_tools_path" in data else None
            self.icon = Path(data.get("icon")) if "icon" in data else None
            self.presplash = Path(data.get("presplash")) if "presplash" in data else None
            self.presplash_color = str(data.get("presplash_color")) if "presplash_color" in data else None
            self.presplash_lottie = Path(data.get("presplash_lottie")) if "presplash_lottie" in data else None
            self.meta_data = dict(data.get("meta_data"))
            self.permissions = list(data.get("permissions"))
            self.gradle_dependencies = list(data.get("gradle_dependencies"))
            self.services = list(data.get("services"))
            self.version_code = int(data.get("version_code")) if "version_code" in data else None
            self.version_name = str(data.get("version_name")) if "version_name" in data else None

    class IOS(EventDispatcher):
        
        bundle_id = StringProperty()
        
        info_plist = DictProperty() # type: dict[str, object] | None
        
        entitlements = DictProperty() # type: dict[str, object] | None
        
        permissions = ListProperty() # type: ListProperty[list[str] | None]
        
        frameworks = ListProperty() # type: ListProperty[list[str] | None]
        
        site_frameworks = ListProperty() # type: ListProperty[list[str] | None]
        
        developer_team = StringProperty()

        def __init__(self, data: dict):
            self.bundle_id = str(data.get("bundle_id"))
            self.info_plist = dict[str, object](data.get("info_plist")) if "info_plist" in data else None
            self.entitlements = dict[str, object](data.get("entitlements")) if "entitlements" in data else None
            self.permissions = list[str](data.get("permissions")) if "permissions" in data else None
            self.frameworks = list[str](data.get("frameworks")) if "frameworks" in data else None
            self.site_frameworks = list[str](data.get("site_frameworks")) if "site_frameworks" in data else None
            self.developer_team = str(data.get("developer_team")) if "developer_team" in data else None

    class MacOS(EventDispatcher):
        
        bundle_id = StringProperty()
        
        info_plist = DictProperty() # type: dict[str, object] | None
        
        entitlements = DictProperty() # type: dict[str, object] | None
        
        permissions = ListProperty() # type: ListProperty[list[str] | None]
        
        frameworks = ListProperty() # type: ListProperty[list[str] | None]
        
        site_frameworks = ListProperty() # type: ListProperty[list[str] | None]
        
        developer_team = StringProperty()
        
        app_category = StringProperty()
        
        app_subcategory = StringProperty()

        def __init__(self, data: dict):
            self.bundle_id = str(data.get("bundle_id"))
            self.info_plist = dict[str, object](data.get("info_plist")) if "info_plist" in data else None
            self.entitlements = dict[str, object](data.get("entitlements")) if "entitlements" in data else None
            self.permissions = list[str](data.get("permissions")) if "permissions" in data else None
            self.frameworks = list[str](data.get("frameworks")) if "frameworks" in data else None
            self.site_frameworks = list[str](data.get("site_frameworks")) if "site_frameworks" in data else None
            self.developer_team = str(data.get("developer_team")) if "developer_team" in data else None
            self.app_category = str(data.get("app_category")) if "app_category" in data else None
            self.app_subcategory = str(data.get("app_subcategory")) if "app_subcategory" in data else None
