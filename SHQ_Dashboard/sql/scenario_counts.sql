
SELECT *
FROM scenarioresults WITH (nolock) 
WHERE  CreatedOn > GETUTCDATE() -
-- GROUP BY CAST(CreatedOn as DATE) 
ORDER BY CAST(CreatedOn as DATE) DESC

SELECT  ScenarioId as Scenario,
	CAST(CreatedOn as DATE) as [Date],
   COUNT(CAST(CreatedOn as DATE)) as ListSize
FROM scenarioresults WITH (nolock) 
WHERE  CreatedOn > GETUTCDATE() -7
GROUP BY ScenarioId,CAST(CreatedOn as DATE) 
ORDER BY Scenario, CAST(CreatedOn as DATE) DESC

select * from ScenarioFile

select * from CampaignCampaign where CampaignID= 4935