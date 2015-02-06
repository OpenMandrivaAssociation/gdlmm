%define url_ver %(echo %{version} | cut -d "." -f -2)

%define api 3.0
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	C++ binding for the gdl library
Name:		gdlmm
Version:	3.7.3
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gdl-3.0) >= 3.7
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.16
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires:	doxygen
BuildRequires:	xsltproc

%description
gdlmm is the C++ binding for the gdl library.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	C++ binding for the gdl library
Group:		System/Libraries

%description -n %{libname}
gdlmm is the C++ binding for the gdl library.

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries and include files for gdlmm
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
gdlmm development files.

%files -n %{devname}
%doc %{_datadir}/doc/gdlmm-%{api}/
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}-%{api}
%{_datadir}/devhelp/books/%{name}-%{api}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh

# first remove outdated generated source files
%configure2_5x
make maintainer-clean

# now build it
%configure2_5x
# generate source files
pushd gdl/src
make all-local
popd
%make

%install
%makeinstall_std

