<h1>Dynamic Connectivity</h1>
<p>In this repo, I put the codes for dynamically connectivity problem in algorithms and data structure. 
Codes are in JS and Python for my personal practice, later on, I may add some code in C++, JAVA 
This material is learned form Algorithms course on <a href="https://www.coursera.org/">Coursera</a>,
and is also available on my <a href="https://www.youtube.com/channel/UCAkzrVPNbgm7rv-DNr14q1Q">YouTube channel</a></p>
<h2>Problem description</h2>
<p>Given a set of N objects, we have to be able to answer these two commands
  <ul>
    <li>union command: connect two objecst</li>
    <li>connected query: is there a path connecting these two objects?</li>
  </ul>
  Is there any path connecting to points?
</p>
<h2>Application</h2>
<p>Applications involve in manipulating objects of all types
  <ul>
    <li>Pixels in a digital photo</li>
    <li>Computers in a network</li>
    <li>Friends in a social network</li>
    <li>Transistors in a computer chip</li>
    <li>Elements in a mathematic set</li>
    <li>Variable name in Fortran program</li>
    <li>Metalic sites in a composite system</li>
  </ul>
</p>

<h2>Assumptions</h2>
<p>We assume that "is connected to" is " s an equivalence relation</p>

<h2>Union-find data type (API)</h2>
<p>Goal: Design effiecient data structure for unin-find
  <ul>
    <li>Number of objects N can be huge</li>
    <li>Number of operations M can be huge</li>
    <li>Find query nad union commands may be intermixed</li>
  </ul>
</p>

<h2>Algorithms</h2>
<ul>
<li>Quick Find</li>
<li>Quick Union</li>
<li>Modified Quick Union</li>
</ul>
