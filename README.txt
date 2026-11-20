ツcore v3.17.0 (Manifest V3, Chrome/Edge)
By ツ / __518_

Load: chrome://extensions -> Developer mode -> Load unpacked -> pick this folder.
Turn MIC ONLY on before joining voice (or rejoin voice after toggling it).

v3.5.0
- Clean voice: 80 Hz high-pass, browser noise suppression on, soft ceiling instead of hard clipping,
  capped post-gain so high gain stays thick instead of buzzing.
- Any mic: auto mic level (boosts quiet mics only, never attenuates), 10 ms latency hint, fallback constraints.
- Music: louder (slider up to 300%, extra makeup gain, bigger gain-follow range) with its own soft saturator.
- Preset save no longer fails where prompt() is blocked.

v3.5.2 (headset mic cut-out fix)
- A temporary OS "mute" on the mic track (Android does this on audio-focus/headset changes) no longer disconnects the mic for good. Only a real "ended" does.
- Noise gate follows the voice level with a ~100 ms hold and slow fade, instead of chopping on single samples.
- MIC ONLY gate is gentler (lower open threshold, longer hold, slower release). Toggling it no longer restarts the live capture; the echo-cancel part applies next time you join voice.
- Old raw mic captures are released on re-join / when Discord stops the track, so only one capture of the headset is open at a time.
- Fallback when constraints fail now keeps your selected headset device instead of switching to the default mic.
- Removed the 10 ms capture-latency request and sampleSize pin (cause underruns on mid-range phones).


v3.6.0 (new look + voice changer)
- New glossy look (still follows the THEME picker), much bigger main button and quick-bar buttons.
- New 🎭 tab: Voice Changer (Chipmunk, Kid, Girl, Man, Deep Monster, Demon, Robot, Alien, Telephone, Radio, Cave, Ghost, Megaphone, Normal).
- Nothing removed: all old tabs, presets, TAFLEH, God Mode, music and mic fixes are unchanged.


v3.7.0 (EAX console look + تفله strength slider)
- New look inspired by Creative EAX Advanced HD console: light panel, classic tabs with arrows, grey slider thumbs, checkbox ticks, glossy blue buttons, blue footer bar with LCD timer.
- تفله is now a strength slider (0-100%) instead of an on/off switch. 0 = off. Higher = taller echo + more reverb bleed.
- Nothing else removed: all tabs, presets, God Mode, voice changer, music and mic fixes are unchanged.


v3.8.0 (POWER update)
- Gain stack much stronger: sliders go to 600, post-gain cap 4x -> 48x, new power-lift stage that keeps the voice dense and loud even on quiet words, hotter output limiter.
- تفله much stronger: harder drive, longer/thicker echo with a second tap, higher feedback, linked to bigger reverb. 100% = maximum.
- Music volume up to 800%, Self Listen up to 500%.
- Girl voice reworked (+ new Soft Girl): smaller pitch jump, less bass, more presence/air, light room.


v3.9.0 (console look like the screenshots + new features)
- Window now matches the Creative console: white header with ? and collapse buttons, tab bar with working left/right arrows, blue transport row (mute, LCD timer, REC, back/play/stop/forward) and navy bottom row (profile pill, shortcut icons, brand).
- EFFECTS tab: Enable Audio Effects, Environment list (Cathedral, Chapel, Church, Concert Hall, Garage, Haunted Cavern, Indoor Arena, Cave, Hangar ...) + Effects Amount slider. Drives the existing reverb / decay / stereo width. Disabling restores your old values. Reverb fine-tune + Mega Reverb moved here.
- KARAOKE tab: Vocal Remover (centre-channel cancel) for the music you play.
- CMSS 3D tab: Off / Headphone / Speaker / Surround modes + Stereo Width + Pan.
- CLEAN-UP tab: Clean voice, Mic Only, Voice Protect, Noise Reduce, Noise Gate, Ducking (moved from FX).
- EQUALIZER tab: 9-band graphic EQ (31 Hz - 8 kHz, +-12 dB) with vertical sliders, Level slider (0 to -24 dB), 16 presets (Classical, Rock, Pop, Jazz, Bass Boost, Vocal Booster ...), save / delete your own presets. Double-click a slider to reset it. Old Bass/Mid/Treble/Air sliders are still there under TONE.
- REC button records your processed output (voice + music) and downloads a .webm. Join voice first.
- Nothing removed: Gain, FX, Music, Voice changer, Presets, Stats, Credits, God Mode, تفله, Self Listen all work as before.

v3.9.1 (POWER EQ)
- EQ bands now go +-24 dB (was +-12) with wider curves, so raising a slider is much louder.
- Level slider now goes from -24 up to +24 dB (was 0 max).
- New presets: MAX POWER, ULTRA BASS, ULTRA VOICE (they also add +6 dB level).

v3.9.2 (look matched to the EAX Console / Graphic Equalizer screenshot)
- Header: device dropdown (shows your real mic once you join voice), cyan window border.
- EFFECTS: environment list in the console order (Auditorium, Ball Park, Bathroom, Cathedral, Chapel, Church, Concert Hall, Garage, Haunted Cavern ...), blue selection, Effects Amount value box.
- EQUALIZER: now a "Graphic Equalizer" window - title bar with device dropdown and ? / reset / X buttons, "Equalizer" bar, Enable Equalizer checkbox, Presets dropdown (<Custom>), 7 bands (125 Hz - 8 kHz) in separate boxes with tick marks, Level slider with live dB readout.
- Enable Equalizer unticked = full bypass (bands + level).
- Bands still go +-24 dB, Level -24..+24 dB, all presets kept (old 31/62 Hz values dropped, saved user presets are converted automatically).

v3.10.2
- Graphic Equalizer: the 31 Hz and 62 Hz bands are back (9 bands again, like v3.9.1). All presets have their full 9 values again. Saved 7-band presets still load.

v3.10.1
- Voice Changer: new "Weak" voice (🥺) - thin, soft, breathy. Nothing else changed.

v3.10.0 (two floating console windows, exactly like the screenshot)
- Click the ツcore button: the EAX-style console (Effects) and the Graphic Equalizer window open side by side. Drag either one by its title bar.
- Console: single wide page bar with < > arrows (and click it for a menu of ALL pages: Karaoke, CMSS 3D, Clean-up, Tone, Gain, FX, Music, Voice, Presets, Stats, Credits, Graphic Equalizer). Blue footer with Default pill + icons; the last icon shows the recorder / transport row (mute, REC, play...).
- "—" shrinks the console to its title bar. In the Equalizer window the blank button shrinks it, X closes it, the footer slider icon reopens it.
- All features are unchanged.

v3.11.0 (pages ported from EAX Console_SVT.exe)
- New THX Setup page: device list + THX modes (Off, Movie, Music, Game, Voice) with an Amount slider. Each mode sets stereo width and the 9-band equalizer.
- New Speakers page (Speaker Settings): layout list (Headphones, 2.0, 2.1, 4.1, 5.1, 7.1, 8.1, 9.1, 10 Speakers) with square speaker boxes you tap on/off. Output is folded to stereo: rear speakers set the width, left/right balance sets the pan, SUB off lowers bass, C off lowers mids.
- New Surround Mixer page: Front balance, Center, Surround, Subwoofer, Rear ambience + reset.
- Nothing removed.

v3.12.0 (exe artwork + live controls)
- New tab "EAX Windows" opens the original EAX Console windows, with the artwork taken from EAX Console_SVT.exe and working controls on top: EAX Console (Effects), Graphic EQ, Surround Mixer, Speaker Settings, THX Setup, CMSS 3D, Clean-up.
- Drag a window by its title bar, close it with X. The little icons in the footer jump between windows.
- Graphic EQ: 7 bands (125 Hz - 8 kHz) and Level, now +-24 dB (labels redrawn); the 31/62 Hz bands stay in the main console EQ.
- Surround Mixer: Volume = master gain, Bass/Treble = tone, Wave/MP3 = music volume, MIDI Synth = air, CD Audio = stereo width, Line-In = input boost, S/PDIF-In = gain 2, CD Digital = reverb, Analog Mix = pan. Speaker buttons mute each one.
- Speaker Settings: tap the speakers in the room picture to switch them on/off (layouts from Headphones to 10 Speakers).
- THX Setup: THX modes row (Off / Movie / Music / Game / Voice) in the dark header.
- Nothing removed.

v3.13.0
- CMSS 3D window now uses the full artwork (Front / Rear box with the speaker pictures); Stereo Focus slider drives stereo width, CMSS / CMSS 2 pick the strength.
- New Time Scaling window (0.50x - 2.00x, centre = Original Speed): speeds up or slows down the music you play. Note: pitch changes with speed (browser limitation).
- Tabs inside the Effects / CMSS / Clean-up / Time Scaling windows now jump between each other.

v3.14.0 (exe look is now the main UI)
- The ツcore button (and Alt+E) now opens the EAX Console and the Graphic Equalizer windows, using the artwork from the exe. The other windows (Surround Mixer, Speaker Settings, THX, CMSS 3D, Clean-up, Time Scaling) open from the footer icons and window tabs.
- The old dark console is still there for the extra tools (voice changer, music loader, presets, God Mode...). Open it with the "?" button in any exe window.
- All artwork is embedded in injector.js, so Discord can't block it. Windows shrink to fit small screens.
IMPORTANT: after installing, press Reload on chrome://extensions and refresh the Discord tab (Ctrl+Shift+R).

v3.15.0 (real reverb presets from ReverbPresets64.dll)
- The 15 environments of the VST (Auditorium, Ball Park, Bathroom, Cathedral, Chapel, Church, Concert Hall, Garage,
  Haunted Cavern, Indoor Arena, Jazz Club, Living Room, Opera House, Small Room, Theater) now use the EXACT EAX 3.0
  numbers stored inside the DLL: room, room HF, decay time, decay HF ratio, reflections level/delay, reverb level/delay,
  environment size, diffusion, echo depth/time, modulation depth/time, default Effects Amount.
- The impulse response is generated from those numbers inside the extension (no DLL needed, works on phones: plain Web Audio).
- Echo and modulation of each preset are applied (modulation = small LFO delay on the reverb output).
- Decay slider now goes to 20 s (Ball Park = 14.7 s, Haunted Cavern = 17 s). The old extra environments are still listed below the 15.
- IMPORTANT: press Reload on chrome://extensions and refresh Discord (Ctrl+Shift+R).
- Reverb slider fix: the amount now controls the SEND into the reverb (before the convolver), not the output. Turning it down
  (even to 0) only stops NEW sound from entering the reverb; the tail that already left your mic keeps ringing and fades out
  by itself. Same for the music reverb.
- With a real preset active the dry voice stays and the reverb is added on top (plugin behaviour), instead of crossfading.
- Equalizer: bands 125 Hz - 8 kHz are now peaking filters with Q = 1.414, exactly like the plugin (read from the DLL code:
  RBJ peaking, 2Q = 2.828, gain/40 dB law). 8 kHz is no longer a shelf. Enable Equalizer off = full bypass.

v3.15.1 (Gain / Songs / Echo & Amplify added from ucore Tsu 3.11)
- NEW windows in the exe look: GAIN (master gain, gain 2, gain 3, input boost, pitch, تفله),
  SONGS (load a song file, play / stop, seek bar, MAX MUSIC) and ECHO & AMPLIFY (music volume + music reverb).
  They drive the same controls as the Gain and Music tabs of Tsu 3.11.
- The first three footer icons (EAX Console and Graphic Equalizer windows, and the new windows) now open: 1 = Gain, 2 = Songs, 3 = Echo & Amplify.
- Deleted: the tab bar of the EAX Console window (Effects / Karaoke / CMSS 3D / Clean-up + arrows)
  and the Presets dropdown of the Graphic Equalizer window.
- Nothing else changed (sizes, look, weights, reverb, EQ are the same as 3.15.0).

v3.15.2 (hiss fix)
- New de-esser on the voice + its reverb (not on music). It cuts the hissy band above 4.5 kHz ("ssss", "tss", spit, reverb-tail hiss)
  only while it sticks out, up to -20 dB, and leaves normal voice untouched. Tested on a real recording: hiss -13 dB, spit -6.5 dB, peak 0.93 -> 0.62.
- Songs window: Music Gain and Music Reverb sliders are inside it.

v3.15.3 (cut-out fix: voice + songs)
- Songs no longer stop when Discord re-grabs the mic (mute/unmute, deafen, channel change, reconnect). The song is resumed from where it was.
- The audio engine (gain / gate / de-esser) is no longer re-registered on every re-join, which could silently drop you into BASIC mode.
- ツcore keeps using the audio context it built its graph in, even if Discord creates other audio contexts later (before, music/sliders could end up on the wrong one).
- If the audio context gets suspended mid-call (focus change, Discord suspending it) it is resumed automatically.
- De-esser no longer allocates memory 375x per second (caused stutter on phones). Same sound.
- Pitch / Voice Changer: click-free pitch shifter (two crossfaded read heads). Only used when pitch is not normal; with pitch normal the sound is bit-for-bit the same as 3.15.2.
- Nothing removed. IMPORTANT: press Reload on chrome://extensions and refresh Discord (Ctrl+Shift+R).

v3.15.4 (song/voice stalls for a few seconds - root cause)
- Found with a screen recording: the song counter ran at 1/3 speed, i.e. the audio engine could not keep up.
- Cause: when the mic is quiet / digitally silent, the 80 Hz high-pass, the envelopes and the de-esser filters decay into
  "denormal" numbers and get stuck there. Every sample was then computed ~10x slower (worse on phone CPUs), the audio thread
  fell behind and the whole audio (voice AND song) froze for seconds until you talked again.
- Fix: tiny filter/envelope states are flushed to exact 0 once per block (below -300 dB, inaudible).
  Measured: engine 34 -> 3.6 us per block in silence, de-esser 65 -> 4.3 us. Output identical to 3.15.3 (difference < 1e-7).
- IMPORTANT: press Reload on chrome://extensions and refresh Discord (Ctrl+Shift+R).

v3.16.0 (dark mixer + anti-cut)
- All EAX windows (Mixer, Effects, EQ, Speakers, THX, CMSS, Clean-up, Time, Gain, Songs, Echo) and the old console are now black instead of white. Button shapes/positions are unchanged.
- LITE mode (turns on by itself for Honor X6c / weak Android phones, and automatically if the audio clock falls behind): bigger output buffer ('playback'), shorter reverb impulses, lighter music saturator, gate holds longer so your voice is not chopped. Echo/Tafleh buffers no longer drift into denormals.
- Manual: in the Discord console run localStorage.n7r_lite='1' (force on) or '0' (force off).
- IMPORTANT: Reload on chrome://extensions and refresh Discord (Ctrl+Shift+R).

v3.16.1 (picture theme)
- The body of every EAX window now shows a picture (Eyas poster) behind the controls. Buttons, sliders and layout are unchanged.
- To use another picture: in injector.js replace the POSTER data-URI (search "PICTURE THEME") and set POSTER_W / POSTER_H to its size. POSTER_DIM (0..1) = how dark the picture is.

v3.17.0 (real reverb back + own picture + self-heal)
- REVERB: the Haunted Cavern (and all 15 environments) are exactly the 3.15 ones again. 3.16's LITE mode used to cut the reverb tail
  to 3 s and switch the music saturator oversampling; that is gone. Verified: the EAX table and the impulse builder are byte-identical to 3.15.2.
  Kept from 3.16 (they do not change the sound): denormal fix, context resume, de-esser, click-free pitch, LITE = bigger output buffer + longer gate hold only.
- PICTURE: new button 🖼 (quick bar, and in the title bar of every window). Choose any image; it is saved in the browser and kept after restart.
  Reset goes back to the skin folder picture / built-in one. Darkness slider included (auto-set for bright pictures).
  Or drop a file named picture.jpg / png / webp / gif into the "skin" folder of the extension (a picture is already there). Then Reload on chrome://extensions.
- SELF-HEAL: if the mic disconnects (headset/USB unplugged, OS takes the mic), is stuck muted, or the audio context gets suspended, ツcore re-opens the mic
  by itself and plugs it into the same graph (no rejoin needed). Discord mute/unmute and leave/rejoin of a room rebuild the graph as before and the song continues.
  New 🔄 button in the quick bar = fix now, by hand.
- IMPORTANT: Reload on chrome://extensions and refresh Discord (Ctrl+Shift+R).
