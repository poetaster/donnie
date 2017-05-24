/**
 * Donnie. Copyright (C) 2017 Willem-Jan de Hoog
 *
 * License: MIT
 */


#ifndef P_UPNP_H
#define P_UPNP_H

#include <QObject>
#include <QVariantList>
#include <QVariantMap>

#include <string>

#include <libupnpp/upnpplib.hxx>
#include <libupnpp/log.hxx>
#include <libupnpp/control/cdirectory.hxx>
#include <libupnpp/control/discovery.hxx>
#include <libupnpp/control/mediarenderer.hxx>
#include <libupnpp/control/renderingcontrol.hxx>

class MprisPlayer;

class UPNP : public QObject
{
    Q_OBJECT
public:
    explicit UPNP(QObject *parent = 0);

    Q_INVOKABLE void init(int search_window = 10);
    //Q_INVOKABLE void search(int search_window = 10);
    //Q_INVOKABLE QVariantList getAdapters();
    //Q_INVOKABLE QVariantMap getRenderers(QString adapter);
    //Q_INVOKABLE QVariantMap getContentDirectories(QString adapter);

    Q_INVOKABLE void discover(int search_window = 10);
    Q_INVOKABLE void browse(QString cid);
    Q_INVOKABLE void browse(QString cid, int startIndex, int maxCount);
    Q_INVOKABLE void search(QString searchString, int startIndex, int maxCount);
    Q_INVOKABLE QString getSearchCapabilitiesJson();
    Q_INVOKABLE QString getParentID(QString id);
    Q_INVOKABLE QString getPathJson(QString id);

    Q_INVOKABLE void getRendererJson(QString friendlyName, int search_window = 10);
    Q_INVOKABLE void getServerJson(QString friendlyName, int search_window = 10);

    //UPnPP::LibUPnP * getLibUPnP();

    Q_INVOKABLE bool setCurrentRenderer(QString name, bool isfriendlyname);
    Q_INVOKABLE bool setCurrentServer(QString name, bool isfriendlyname);

    UPnPClient::MRDH getRenderer(QString name, bool isfriendlyname);
    UPnPClient::CDSH getServer(QString name, bool isfriendlyname);

    // for renderer
    Q_INVOKABLE int play();
    Q_INVOKABLE int pause();
    Q_INVOKABLE int stop();
    Q_INVOKABLE int setVolume(int volume);
    Q_INVOKABLE int getVolume();
    Q_INVOKABLE bool getMute();
    Q_INVOKABLE int setMute(bool mute);
    Q_INVOKABLE int setTrack(QString uri, QString didl);
    Q_INVOKABLE int setNextTrack(QString uri, QString didl);
    Q_INVOKABLE int seek(int seconds);

    Q_INVOKABLE QString getTransportInfoJson();
    Q_INVOKABLE QString getPositionInfoJson();
    Q_INVOKABLE QString getMediaInfoJson();

    Q_INVOKABLE void getTransportInfoJsonAsync();

    // for mpris control
    Q_INVOKABLE void mprisPlay();
    Q_INVOKABLE void mprisPause();
    Q_INVOKABLE void mprisNext();
    Q_INVOKABLE void mprisPrevious();
    // 0x01: play, 0x02: pause, 0x04: next, 0x08: previous
    // 0x0100: playing, 0x0200: paused
    Q_INVOKABLE void mprisSetStateMask(unsigned int mask);
    Q_INVOKABLE void mprisSetMetaData(QString metaDataJson);

signals:
    void getRendererDone(QString rendererJson);
    void getServerDone(QString serverJson);
    void discoveryDone(QString devicesJson);
    void browseDone(QString contentsJson);
    void searchDone(QString searchResultsJson);
    void error(QString msg);
    void mprisControl(QString action);
    void transportInfo(QString transportInfoJson);

public slots:
    void onGetRendererDone(QString rendererJson);
    void onGetServerDone(QString serverJson);
    void onDiscoveryDone(QString devicesJson);
    void onBrowseDone(QString contentsJson);
    void onSearchDone(QString searchResultsJson);
    void onError(QString msg);
    void onTransportInfo(QString transportInfoJson);

protected:
    UPnPP::LibUPnP * libUPnP;
    UPnPClient::UPnPDeviceDirectory *superdir;
    UPnPClient::MRDH currentRenderer;
    UPnPClient::CDSH currentServer;

    MprisPlayer *mprisPlayer;

};

#endif // P_UPNP_H
