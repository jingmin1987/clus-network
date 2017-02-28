# clus-network
A network visualization to show
* How SAS' Proc Varclus groups the existing variables 
* Where the new variables fit into the current structure

# Purpose
The idea behind this visualization is to explore new variables from LexisNexis to see if they can provide any additional information structure-wise (less correlated with existing structure). This information is then combined with IV or Gini statistics to filter the strong and less-correlated ones.

# Interactive Graph
In the following graph, each edge represents a correlation bound that is above 0.5 and each node is either a cluster component (big circle), or existing variables (small circle) or LexisNexis variables (x shape).

Please click on the following graph for interaction.

<div>
    <a href="https://plot.ly/~jingmin1987/2/?share_key=1NeKzz7Di6fh2akYdiYh35" target="_blank" title="varclus" style="display: block; text-align: center;"><img src="https://plot.ly/~jingmin1987/2.png?share_key=1NeKzz7Di6fh2akYdiYh35" alt="varclus" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="jingmin1987:2" sharekey-plotly="1NeKzz7Di6fh2akYdiYh35" src="https://plot.ly/embed.js" async></script>
</div>
