%define url_ver %(echo %{version} | cut -d "." -f -2)

%define api_version	3.0
%define lib_major	1
%define lib_name	%mklibname %{name} %{api_version} %{lib_major}
%define develname	%mklibname -d %{name}

Summary:	C++ binding for the gdl library
Name:		gdlmm
Version:	3.3.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		gdlmm-3.3.2-gdl_dock_layout_run_manager.patch
BuildRequires: pkgconfig(gdl-3.0) >= 3.0
BuildRequires: pkgconfig(glibmm-2.4) >= 2.16
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.0

%description
gdlmm is the C++ binding for the gdl library.


#--------------------------------------------------------------------

%package -n %{lib_name}
Summary: C++ binding for the gdl library
Group: System/Libraries

%description -n %{lib_name}
gdlmm is the C++ binding for the gdl library.

%files -n %{lib_name}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgdlmm-%{api_version}.so.%{lib_major}*

#--------------------------------------------------------------------

%package -n %develname
Summary:        Libraries and include files for gdlmm
Group:          Development/C++
Requires: 	%lib_name = %version
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
gdlmm development files. 

%files -n %develname
%doc %_datadir/doc/gdlmm-%{api_version}/
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}-%{api_version}
%{_datadir}/devhelp/books/%{name}-%{api_version}

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -fr %buildroot%_libdir/*.la



%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.3.2-1
+ Revision: 796894
- imported package gdlmm

