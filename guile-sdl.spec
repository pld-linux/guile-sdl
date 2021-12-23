Summary:	Guile-SDL - set of modules that provide Guile bindings for SDL
Summary(pl.UTF-8):	Guile-SDL - zestaw modułów zapewniających wiązania Guile do SDL
Name:		guile-sdl
Version:	0.5.3
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/guile-sdl/%{name}-%{version}.tar.lz
# Source0-md5:	0d0a85c0170c6169586ac98d3558b6a3
Patch0:		%{name}-info.patch
Patch1:		%{name}-somode.patch
URL:		http://www.gnu.org/software/guile-sdl/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_gfx-devel >= 2.0.22
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.12.2
BuildRequires:	guile-devel >= 5:1.4
BuildRequires:	libtool >= 2:2.4.2
BuildRequires:	lzip
BuildRequires:	texinfo
BuildRequires:	tar >= 1:1.22
Requires(post,postun):	/sbin/ldconfig
Requires:	SDL >= 1.2.0
Requires:	SDL_gfx >= 2.0.22
Requires:	guile >= 5:1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Guile-SDL, a set of modules that provide
bindings for SDL (Simple DirectMedia Layer) to enable Guile
programmers to do all the nice things you can do with SDL.

Most of the SDL functions have been wrapped with the exception of a
few functions that were too C-centric. The SDL Threads and the Audio
functions haven't been included because of the problems with Guile
code being run from more than one thread. However audio programming
can be done with the module (sdl mixer) that requires the SDL_mixer
library. Bindings for SDL_gfx are also included.

%description -l pl.UTF-8
Ten pakiet zawiera Guile-SDL - zbiór modułów będących wiązaniami do
bibliotek SDL (Simple DirectMedia Layer), pozwalających programistom
Guile robić wszystkie przyjemne rzeczy, które można robić z użyciem
SDL-a.

Obudowanych jest większość funkcji SDL-a z wyjątkiem kilku, które były
zbyt C-centryczne. Funkcje dotyczące wątków (SDL Threads) i dźwięku
(SDL Audio) nie zostały dołączone ze względu na problemy z działaniem
kodu Guile w więcej niż jednym wątku. Pprogramowanie dźwięku jest
jednak możliwe przy użyciu modułu (sdl mixer), wymagającego biblioteki
SDL_mixer. Dołączone są także wiązania do biblioteki SDL_gfx.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I build-aux
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-embedded-gfx

# build is racy (generating some files vs compilation)
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY NEWS README THANKS ugh/*.sed
%dir %{_libdir}/guile-sdl
%attr(755,root,root) %{_libdir}/guile-sdl/gfx.so
%attr(755,root,root) %{_libdir}/guile-sdl/mixer.so
%attr(755,root,root) %{_libdir}/guile-sdl/sdl.so
%attr(755,root,root) %{_libdir}/guile-sdl/ttf.so
%dir %{_datadir}/guile/site/sdl
%{_datadir}/guile/site/sdl/gfx
%{_datadir}/guile/site/sdl/misc-utils.scm
%{_datadir}/guile/site/sdl/mixer
%{_datadir}/guile/site/sdl/sdl
%{_datadir}/guile/site/sdl/simple.scm
%{_datadir}/guile/site/sdl/ttf
%{_infodir}/guile-sdl.info*
