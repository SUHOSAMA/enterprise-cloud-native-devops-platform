resource "aws_eks_cluster" "main" {
  name     = var.eks_cluster_name
  role_arn = "arn:aws:iam::640440228485:role/eksClusterRole"

  version = "1.35"

  vpc_config {
    subnet_ids = aws_subnet.private[*].id

    endpoint_private_access = true
    endpoint_public_access  = true
  }

  enabled_cluster_log_types = [
    "api",
    "audit",
    "authenticator",
    "controllerManager",
    "scheduler"
  ]

  tags = {
    Name = var.eks_cluster_name
  }

  depends_on = [
    aws_vpc.main,
    aws_nat_gateway.main
  ]
}

resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${var.eks_cluster_name}-nodes"
  node_role_arn   = "arn:aws:iam::640440228485:role/eksNodeRole"

  subnet_ids = aws_subnet.private[*].id

  instance_types = [
    var.eks_node_instance_type
  ]

  capacity_type = "ON_DEMAND"

  scaling_config {
    desired_size = var.eks_desired_nodes
    min_size     = var.eks_min_nodes
    max_size     = var.eks_max_nodes
  }

  update_config {
    max_unavailable = 1
  }

  labels = {
    workload = "application"
  }

  tags = {
    Name = "${var.eks_cluster_name}-node-group"
  }

  depends_on = [
    aws_eks_cluster.main
  ]
}
