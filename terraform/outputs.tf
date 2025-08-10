output "website_endpoint" {
  value       = aws_s3_bucket_website_configuration.website.website_endpoint
  description = "The website endpoint of the S3 bucket"
}
output "hosted_zone_name_servers" {
  description = "The name servers for the Route 53 hosted zone"
  value       = aws_route53_zone.main.name_servers
}

output "visitor_counter_api_endpoint" {
  value       = aws_apigatewayv2_api.visitor_counter_api.api_endpoint
  description = "The HTTP endpoint for the visitor counter API"
}

#add output for cloudfront distribution ID
output "cloudfront_distribution_id" {
  value       = aws_cloudfront_distribution.website.id
  description = "The ID of the CloudFront distribution"
}