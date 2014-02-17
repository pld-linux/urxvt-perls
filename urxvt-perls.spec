# NOTE
# - not noarch due package dir
%include	/usr/lib/rpm/macros.perl
Summary:	A small collection of Perl extensions for the rxvt-unicode terminal emulator
Name:		urxvt-perls
Version:	2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://github.com/muennich/urxvt-perls/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	656dace02d55536954154f530e8a0cb3
URL:		http://github.com/muennich/urxvt-perls
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	urxvt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		urxvtperldir %{_libdir}/urxvt/perl

# no arch specific blobs
%define		_enable_debug_packages	0

%description
A small collection of Perl extensions for the rxvt-unicode terminal
emulator.

%prep
%setup -q

%{__sed} -i -e '1s,#!.*perl,#!%{__perl},' *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{urxvtperldir}
install -p clipboard $RPM_BUILD_ROOT%{urxvtperldir}
install -p keyboard-select $RPM_BUILD_ROOT%{urxvtperldir}
install -p url-select $RPM_BUILD_ROOT%{urxvtperldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{urxvtperldir}/clipboard
%{urxvtperldir}/keyboard-select
%{urxvtperldir}/url-select
