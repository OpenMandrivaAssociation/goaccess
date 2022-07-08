Name:           goaccess
Version:	1.6.1
Release:	1
Summary:        Real-time web log analyzer and interactive viewer
License:        GPLv2+
URL:            http://goaccess.io/
Source0:        http://tar.goaccess.io/goaccess-%{version}.tar.gz
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)


%description
GoAccess is a real-time web log analyzer and interactive viewer that runs in a
terminal in *nix systems. It provides fast and valuable HTTP statistics for
system administrators that require a visual server report on the fly.

Features:
GoAccess parses the specified web log file and outputs the data to terminal.

* General statistics, bandwidth, etc.
* Time taken to serve the request (useful to track pages that are slowing down.
your site).
* Metrics for cumulative, average and slowest running requests.
* Top visitors.
* Requested files & static files.
* 404 or Not Found.
* Hosts, Reverse DNS, IP Location.
* Operating Systems.
* Browsers and Spiders.
* Referring Sites & URLs.
* Keyphrases.
* Geo Location - Continent/Country/City.
* Visitors Time Distribution.
* HTTP Status Codes.
* Ability to output JSON and CSV.
* Tailor GoAccess to suit your own color taste/schemes.
* Support for large datasets + data persistence.
* Support for IPv6.
* Output statistics to HTML. 
and more...

GoAccess allows any custom log format string. Predefined options include, but
not limited to:

* Amazon CloudFront (Download Distribution).
* AWS Elastic Load Balancing.
* Apache/Nginx Common/Combined + VHosts.
* Google Cloud Storage.
* W3C format (IIS).

%prep
%setup -q
%configure --enable-debug --enable-geoip=mmdb --enable-utf8

%build
%make_build

%install
%make_install
%find_lang goaccess

%files -f goaccess.lang
%doc AUTHORS ChangeLog README TODO COPYING
%dir %{_sysconfdir}/goaccess
%config(noreplace) %{_sysconfdir}/goaccess/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
