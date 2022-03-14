# PMTtoDDS
PixelTales texture Header Fixer

This tool exist for "fixing" texture files from games like Star Stable 1-4, Star Academy 1-4, Springdale

the textures are inside data.csa which you can extract by using https://github.com/ermaccer/CSAExtractor<br>
from there get .pmt files, these are actually dds files but with some junk in the headder<br>
my tool removes the junk from the headder and gives you a dds file you can open in GIMP

I am planning on implementing the reverse of this, putting dds files back into the game<br>
but for that I need to do more experimenting so not yet.

I could also implement .pso to .wav conversion which is just renaming files.

file info about PixelTale games:<br>
.pso -> .wav (audio files)<br>
.pmt -> .dds (textures)
