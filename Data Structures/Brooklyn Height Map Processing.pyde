import copy
import xml.etree.ElementTree as etree

def getMap(file):
    """
This loads the map and returns a pair (V,E)
V contains the coordinates of the veritcies
E contains pairs of coordinates of the verticies
"""
    G=open(file)   
    root = etree.parse(G).getroot()
    v={}
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e

class Graph:
  """Representation of a simple graph using an adjacency map."""

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'
  
    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x
  
    def element(self):
      """Return element associated with this vertex."""
      return self._element
  
    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)
    
  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin', '_destination', '_element'
  
    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x
  
    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)
  
    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')
  
    def element(self):
      """Return element associated with this edge."""
      return self._element
  
    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')
    
  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):   
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v
      
  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.get_edge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e
    
def drawEdge(e):
            line(e.endpoints()[0].element()[0],
                e.endpoints()[0].element()[1],
                e.endpoints()[1].element()[0],
                e.endpoints()[1].element()[1])
    

class Map:
    def __init__(self,file):
        (V,E)=getMap(file)
        self._G=Graph()
        self._V={}
        for v in V:
            self._V[v]=self._G.insert_vertex(v)
        for e in E:
            try:
                self._G.insert_edge(self._V[e[0]],self._V[e[1]],e)
            except ValueError:
                pass
        print("Loaded map with "+str(self._G.vertex_count())+" verticies and "+
              str(self._G.edge_count())+" edges.")
    def draw(self):
        for e in self._G.edges():
            drawEdge(e)
            
    def drawClosest(self,x,y):    
        closest=min(self._G.edges(),
                    key=lambda(e):min(dist(e.endpoints()[0].element()[0],
                                       e.endpoints()[0].element()[1],
                                       x,y),
                                  dist(e.endpoints()[1].element()[0],
                                       e.endpoints()[1].element()[1],
                                       x,y)))

        strokeWeight(0.0002)
        stroke(0,255,0)
        drawEdge(closest)
        strokeWeight(0.00001)
        stroke(255,0,0)
        drawEdge(closest)
        level = [closest]
        nextlevel = []
        discovered = set()
        discovered.add(closest)
        distance=1
        while level:
            stroke(max(0,255-5*distance),0,255-max(0,255-5*distance))
            distance+=1
            for e in level:
                for v in e.endpoints():
                    for ie in self._G.incident_edges(v):
                        if ie not in discovered:
                            discovered.add(ie)
                            drawEdge(ie)
                            nextlevel.append(ie)
            level,nextlevel=nextlevel,[]
         
def mouseToScreen(mx,my):
    return (minlon+(mx/float(width))*(maxlon-minlon),
            minlat+(my/float(height))*(maxlat-minlat))
            
def setup():
    size(2160,1440)
    pixelDensity(displayDensity())
    global M,maxlat,maxlon,minlat,minlon
    M=Map("map.osm")
    maxlat=40.6903
    minlat=40.7061
    maxlon=-73.9728
    minlon=-74.0065 
    
def draw():
    background(255)
    scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
    stroke(0)
    translate(-minlon,-minlat)
    stroke(128)
    strokeWeight(0.00001)
    M.draw()
    M.drawClosest(*mouseToScreen(mouseX,mouseY))