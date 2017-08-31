Name:           ros-jade-novatel-gps-driver
Version:        3.3.0
Release:        0%{?dist}
Summary:        ROS novatel_gps_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libpcap-devel
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-gps-common
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nodelet
Requires:       ros-jade-novatel-gps-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-swri-math-util
Requires:       ros-jade-swri-nodelet
Requires:       ros-jade-swri-roscpp
Requires:       ros-jade-swri-serial-util
Requires:       ros-jade-swri-string-util
Requires:       ros-jade-tf
BuildRequires:  boost-devel
BuildRequires:  libpcap-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-gps-common
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-novatel-gps-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-swri-math-util
BuildRequires:  ros-jade-swri-nodelet
BuildRequires:  ros-jade-swri-roscpp
BuildRequires:  ros-jade-swri-serial-util
BuildRequires:  ros-jade-swri-string-util
BuildRequires:  ros-jade-tf

%description
Driver for NovAtel receivers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Aug 31 2017 P. J. Reed <preed@swri.org> - 3.3.0-0
- Autogenerated by Bloom

